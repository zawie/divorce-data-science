from sklearn import svm
from sklearn.model_selection import cross_validate
import data
import time
import copy

removed = []

inputs, categories = data.get_shuffled()

#TODO: switch to True once we actually want to run it
while len(data) > 0:
    lowest_impact_idx = 0
    lowest_impact_cv_results = None
    for idx in range(categories):
        temp_inputs = copy.deepcopy(inputs)
        temp_categories = copy.deepcopy(categories)
        temp_inputs.pop(idx)
        temp_categories.pop(idx)

        clf = svm.SVC()
        cv_results = cross_validate(clf, temp_inputs, temp_categories, cv=2)
        results = data.assess_results(cv_results)
        if lowest_impact_cv_results is None or results < lowest_impact_cv_results:
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