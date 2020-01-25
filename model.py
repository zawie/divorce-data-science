from sklearn import svm
from sklearn.model_selection import cross_validate
import data
import time

removed = []

inputs, categories = data.get_shuffled()

#TODO: switch to True once we actually want to run it
while False:
    #Ends once there are only this many questions left
    if len(data) == 10:
        break
    lowest_impact_idx = 0
    lowest_impact_cv_results = "temp"
    for idx in range(categories):
        clf = svm.SVC()
        cv_results = cross_validate(clf, inputs, categories, cv=2)
        results = data.assess_results(cv_results)
        if results < lowest_impact_cv_results:
            lowest_impact_idx = idx
            lowest_impact_cv_results = results

    #Put the break if accuracy gets too low here

    #Stores info about the removed row
    #(data in row, category of row, results of removal)
    lowest_val_row = (data.pop(lowest_impact_idx), categories(lowest_impact_idx), lowest_impact_cv_results)
    removed.append(lowest_val_row)

inputs, categories = data.get_shuffled()
clf = svm.SVC()
cv_results = cross_validate(clf,inputs,categories,cv=5)
print(cv_results)