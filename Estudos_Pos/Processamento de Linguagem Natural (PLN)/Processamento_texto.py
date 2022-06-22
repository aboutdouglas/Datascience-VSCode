import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import string
import pandas as pd

imdb = pd.read_csv('https://drive.google.com/u/0/uc?id=1ZlZsxrMHhZZb9ZTYABOiWw7bCPofY6cz&export=download', header=0)

exemplo = imdb['review'].values[0]
print(exemplo)
print(len(exemplo.split()))

stopwords = nltk.corpus.stopwords.words('english')
ponctuations = list(string.punctuation)
TAMANHO_MINIMO = 1
IGNORAR = ['....', '...', 'br', '.so', 'll', '']
stemmer = SnowballStemmer('english')

def prepara(texto):
    palavras = [i for i in word_tokenize(texto, language='english') if i not in string.punctuation]
    palavras = [i for i in palavras if i not in stopwords]
    palavras = [i for i in palavras if len(i) > TAMANHO_MINIMO]
    palavras = [i for i in palavras if i not in IGNORAR]
    palavras = [stemmer.stem(i) for i in palavras]
    return palavras

exemplo_preparado = prepara(exemplo)
print(exemplo_preparado)
print(len(exemplo_preparado))

imdb['review2'] = imdb['review'].apply(prepara)
imdb['review2'] = imdb['review2'].apply(''.join)
print(imdb.head())
