import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, plot_confusion_matrix
from Treino_Teste import bow_X_train, bow_X_test, ohe_y_train, ohe_y_test

lr = LogisticRegression(penalty='l2', max_iter=500, C=1, random_state=42)
lr.fit(bow_X_train, ohe_y_train.ravel())
print(lr)

y_predict = lr.predict(bow_X_test)
print("LogReg Score:", accuracy_score(ohe_y_test, y_predict))
print(classification_report(ohe_y_test, y_predict, target_names=['Positive', 'Negative']))
plot_confusion_matrix(lr, bow_X_test, ohe_y_test, values_format='d');
plt.show()
