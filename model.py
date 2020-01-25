from sklearn import svm
import data

x_train, y_train, x_test, y_test = data.split(.8)

clf = svm.SVC()
clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))
