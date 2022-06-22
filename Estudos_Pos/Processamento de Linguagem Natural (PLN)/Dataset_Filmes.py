import matplotlib.pyplot as plt
import pandas as pd

imdb = pd.read_csv('C:\\Users\QUALITOR.QPOA000006\Desktop\Python\Estudos_Pos\Processamento de Linguagem Natural (PLN)\IMDB_Dataset.csv', header=0)

filmes = pd.DataFrame(imdb)

print(filmes.head())

print(filmes.isnull().sum())

print(filmes['sentiment'].value_counts())

filmes['sentiment'].value_counts().plot.bar(title='Quantidade por Tipo',rot=90)
plt.show()
