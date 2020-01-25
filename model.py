from sklearn import svm
from sklearn.model_selection import cross_validate
import data
import time

X,y = data.get()

clf = svm.SVC()
cv_results = cross_validate(clf, X, y, cv=2)
print(cv_results)

