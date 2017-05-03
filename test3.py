import nltk as nl
from nltk.corpus import stopwords
from nltk.corpus import genesis

text = "My name is not King Mr. Piotr"

tokens = nl.tokenize.word_tokenize(text)

stop = set(stopwords.words("english"))
nonoise_text = [x for x in tokens if not x in stop]

print(genesis.fileids())

bookofGenesis = genesis.raw('english-kjv.txt')
print(bookofGenesis)
