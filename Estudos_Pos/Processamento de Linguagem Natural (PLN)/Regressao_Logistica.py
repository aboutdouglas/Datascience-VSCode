from pandas import lreshape
from sklearn.linear_model import LogisticRegression
from Treino_Teste import bow_X_train, ohe_y_train

lr = LogisticRegression(penalty='l2', max_iter=500, C=1, random_state=42)
lr.fit(bow_X_train, ohe_y_train.ravel())
print(lr)
