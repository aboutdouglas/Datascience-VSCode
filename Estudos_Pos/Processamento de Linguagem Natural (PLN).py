from xml.sax.handler import feature_external_ges
from matplotlib.pyplot import text
import nltk
from string import punctuation
from nltk.corpus import machado
from nltk.tokenize import sent_tokenize,word_tokenize
from sklearn.feature_extraction.text import CountVectorizer


machado.fileids()

texto = machado.raw('romance/marm05.txt')
texto = texto[10082:10954].replace('\n',' ')
print(texto)

sentencas = sent_tokenize(texto, language='portuguese')
for i,sent in enumerate(sentencas):
     sent_sem_pontuacao = [i for i in word_tokenize(sent, language='portuguese') 
                           if i not in punctuation]
     stopwords = nltk.corpus.stopwords.words('portuguese')
     print(stopwords)
     sent_sem_stopwords = [i for i in sent_sem_pontuacao if i not in stopwords]
     print(i,'-',sent_sem_stopwords)
     print(i,'-',sent_sem_pontuacao)
    
cv = CountVectorizer(min_df=0,max_df=1,binary=False,ngram_range=(1,1))    
bow = cv.fit_transform(sentencas)
print('BoW Shape:',bow.shape)
print('BoW Vocabulário (',len(cv.vocabulary_),'palavras ):',cv.vocabulary_)
print('Primeira sentença:',bow[0].toarray())
print('Segunda sentença:',bow[1].toarray())
