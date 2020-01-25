from sklearn import svm
from sklearn.model_selection import cross_validate
import data
import time
import copy

removed = []
inputs, labels = data.get_shuffled()
num_rows = len(inputs)

def trainAndTest(X,y):
    clf = svm.SVC()
    cv_results = cross_validate(clf, X, y, cv=2)
    results = data.assess_results(cv_results)
    average_accuracy = mean(results)
    return average_accuracy

def getColumns():
    return len(inputs[0])

def removeColumn(X,col):
    rem_col = []
    for r in len(X):
        rem_col.append(X[r].pop(col))
    return rem_col

#TODO: switch to True once we actually want to run it

while getColumns() > 0:
    num_columns = getColumns()
    lowest_impact_idx = 0
    lowest_impact_cv_results = None
    for c in num_columns:
        #copy and remove column
        temp_inputs = copy.deepcopy(inputs)
        removeColumn(temp_inputs,c)
        #train & test
        average_accuracy = trainAndTest(temp_inputs,labels)
        if (lowest_impact_cv_results is None)or (average_accuracy < lowest_impact_cv_results):
            lowest_impact_idx = c
            lowest_impact_cv_results = average_accuracy

    #Put the break if accuracy gets too low here

    #Stores info about the removed row
    #(data in row, category of row, results of removal)
    lowest_val_col = (removeColumn(inputs), lowest_impact_idx, lowest_impact_cv_results, len(inputs[0]))
    removed.append(lowest_val_col)

inputs, categories = data.get_shuffled()
clf = svm.SVC()
cv_results = cross_validate(clf,inputs,categories,cv=5)
print(cv_results)