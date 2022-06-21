# Importando Bibliotecas
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Importando o modelo Naive Bayes
from sklearn.naive_bayes import GaussianNB

# Carregando os dados
X, y = load_iris(return_X_y=True)

# Separando a base de treino da validação
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5, random_state=0)

# Criando classificadores
gnb = GaussianNB()

# Treinando o classificador
gnb.fit(X_train, y_train)

# Realizando as previsões
y_pred = gnb.predict(X)
