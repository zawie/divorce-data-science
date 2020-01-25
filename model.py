from sklearn import svm
import data

X,y = data.get()

train,test = data.split(X,120)
print(len(train),len(test))

#clf = svm.SVC()
#clf.fit(X, y)

#print(clf.predict(inputs))