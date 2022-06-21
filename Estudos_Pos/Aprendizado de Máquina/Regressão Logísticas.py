from distutils.log import Log
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

lr = LogisticRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X)
