from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelBinarizer
from Processamento_texto import imdb

X_train, X_test, y_train, y_test = train_test_split(imdb['review2'], imdb['sentiment'], test_size=0.2, random_state=0)

print('X_train shape:',X_train.shape)
print('y_train shape:',y_train.shape)
print('X_test shape:',X_test.shape)
print('y_test shape:',y_test.shape)

cv = CountVectorizer(min_df=0,max_df=1,binary=False,ngram_range=(1,1))
bow_X_train = cv.fit_transform(X_train)
bow_X_test = cv.transform(X_test)
print('bow_X_train shape:', bow_X_train.shape)
print('bow_X_test shape:', bow_X_test.shape)

lb = LabelBinarizer()
ohe_y_train = lb.fit_transform(y_train)
ohe_y_test = lb.fit_transform(y_test)
print('ohe_y_train shape:', ohe_y_train.shape)
print('ohe_y_test shape:', ohe_y_test.shape)
