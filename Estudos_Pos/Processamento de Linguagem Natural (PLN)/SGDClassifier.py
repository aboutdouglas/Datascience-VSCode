import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report, plot_confusion_matrix
from Treino_Teste import bow_X_train, bow_X_test, ohe_y_train, ohe_y_test

svm = SGDClassifier(loss='hinge', random_state=42)
svm.fit(bow_X_train,ohe_y_train.ravel())

y_predict = svm.predict(bow_X_test)
print("SVM Score:", accuracy_score(ohe_y_test, y_predict))
print(classification_report(ohe_y_test, y_predict, target_names=['Positive', 'Negative']))
plot_confusion_matrix(svm, bow_X_test, ohe_y_test, values_format='d');
plt.show()
