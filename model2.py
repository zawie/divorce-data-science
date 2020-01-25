from sklearn import svm
from sklearn.svm import SVC
from sklearn.model_selection import cross_validate
from sklearn.datasets import load_digits
from sklearn.feature_selection import RFE
import data
import time
import copy
import matplotlib.pyplot as plt

inputs, labels = data.get_shuffled()

def getColumns():
    return len(inputs[0])

def getAccuracy(X,y):
    clf = svm.SVC()
    cv_results = cross_validate(clf, X, y, cv=5)
    results = data.assess_results(cv_results)
    average_accuracy = sum(cv_results['test_score'])/len(cv_results['test_score'])
    return average_accuracy

def getWorstColumn(X,y):
    svc = SVC(kernel="linear", C=1)
    rfe = RFE(estimator=svc, n_features_to_select=getColumns()-1, step=1)
    rfe.fit(X, y)
    support = list(rfe.support_)
    #return worst
    for i in range(len(support)):
        if not support[i]:
            return i

def removeColumn(X,col):
    for r in range(len(X)):
        X[r].pop(col)

def trial():
    results = []
    x_axis = []
    y_axis = []
    while getColumns() > 1:
        worst_column = getWorstColumn(inputs,labels)
        removeColumn(inputs, worst_column)
        accuracy = getAccuracy(inputs,labels)
        point = (getColumns(),accuracy)
        x_axis.append(point[0])
        y_axis.append(point[1])
        #print(point)
        results.append(point)
    return results

family = dict()
for t in range(100):
    print("Trial",t)
    results = trial()
    for point in results:
        x = point[0]
        y = point[1]
        if x not in family:
            family[x] = []
        family[x].append(y)
    inputs, labels = data.get_shuffled() #restore data

x_axis = []
y_axis = []
for key,values in family.items():
    x_axis.append(key)
    average = sum(values)/len(values)
    y_axis.append(average)

plt.plot(x_axis,y_axis)
plt.show()