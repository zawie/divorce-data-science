from sklearn import svm
import data


X,y= data.get()
num_inputs = len

print(X,y)
#X = [[0, 0], [1, 1]] #inputs
#y = [0, 1] #groups

clf = svm.SVC()
clf.fit(X, y)
print(clf.predict([[0]*len(X[0])]))