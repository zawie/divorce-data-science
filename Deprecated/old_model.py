from sklearn import svm
from sklearn.model_selection import cross_validate
import data
import time
import copy
import matplotlib.pyplot as plt

removed = []
inputs, labels = data.get_shuffled()
num_rows = len(inputs)

def trainAndTest(X,y):
    total_acc = 0
    run_times = 10
    for i in range(run_times):
        clf = svm.SVC()
        cv_results = cross_validate(clf, X, y, cv=3)
        results = data.assess_results(cv_results)
        average_accuracy = sum(cv_results['test_score'])/len(cv_results['test_score'])
        total_acc += average_accuracy
    return total_acc/run_times

def getColumns():
    """
    Inputs: None
    Outputs: Number of columns in input. 
    (Note, inputs is constantly modified)
    """
    return len(inputs[0])

def removeColumn(X,col):
    rem_col = []
    for r in range(len(X)):
        rem_col.append(X[r].pop(col))
    return rem_col

while getColumns() > 1:
    num_columns = getColumns()
    lowest_impact_idx = 0
    lowest_impact_cv_results = None
    for c in range(num_columns):
        #copy and remove column
        temp_inputs = copy.deepcopy(inputs)
        removeColumn(temp_inputs,c)
        #train & test
        average_accuracy = trainAndTest(temp_inputs,labels)
        if (lowest_impact_cv_results is None) or (average_accuracy > lowest_impact_cv_results):
            lowest_impact_idx = c
            lowest_impact_cv_results = average_accuracy

    #Put the break if accuracy gets too low here

    #Stores info about the removed row
    #(data in row, category of row, results of removal)
    lowest_val_col = (removeColumn(inputs, lowest_impact_idx), lowest_impact_cv_results, len(inputs[0]))
    removed.append(lowest_val_col)
    print("removed", len(inputs[0]))

num_remaining = []
accuracy = []
for dat_point in removed:
    num_remaining.append(dat_point[2])
    accuracy.append(dat_point[1])

plt.plot(num_remaining, accuracy)
plt.show()
for dat in removed:
    print(dat[1:])
"""
inputs, categories = data.get_shuffled()
print(trainAndTest(inputs, categories))
#clf = svm.SVC()
#cv_results = cross_validate(clf,inputs,categories,cv=5)
#print(cv_results)
"""