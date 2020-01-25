from sklearn import svm
from sklearn.svm import SVC
from sklearn.model_selection import cross_validate
from sklearn.datasets import load_digits
from sklearn.feature_selection import RFE
import data
import time
import copy
import matplotlib.pyplot as plt

X,y = data.get_shuffled()

svc = SVC(kernel="linear", C=1)
rfe = RFE(estimator=svc, n_features_to_select=1, step=1)
rfe.fit(X, y)
support = list(rfe.support_)
ranking  = list(rfe.ranking_)
print(ranking)