# importando as bibliotecas
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# importando o modelo árvore de decisão
from sklearn.tree import DecisionTreeClassifier

# carregando os dados
X, y = load_iris(return_X_y=True)

# separando a base de treinamento da validação
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

# criando o classificador
dtc = DecisionTreeClassifier()

# treinando o classificador
dtc.fit(X_train, y_train)

# realizando as previsões
y_pred = dtc.predict(X)
