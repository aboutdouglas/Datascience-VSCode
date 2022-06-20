
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

clf = SVC(kernel='linear', C=1.0)
clf.fit(X_train, y_train)
pred = clf.predict(X)

print(pred)
