import nltk
from nltk.corpus import genesis
# from nltk.corpus import gutenberg
from nltk.corpus import stopwords

print(genesis.fileids())
# print(gutenberg.fileids())
genesis_book = genesis.raw('english-kjv.txt')
# bible = gutenberg.raw('bible-kjv.txt')

# tokenized_bible = nltk.tokenize.word_tokenize(bible)
tokenized_genesis = nltk.tokenize.word_tokenize(genesis_book)

# print(len(tokenized_bible))
print(len(tokenized_genesis))

stop_words = set(stopwords.words("english"))
tokenized_genesis_nostop = [x for x in tokenized_genesis if not x in stop_words]

print(len(tokenized_genesis_nostop))
# print(len(tokenized_genesis))
print(tokenized_genesis)
print(tokenized_genesis_nostop)

