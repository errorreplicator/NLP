import nltk
from nltk.corpus import stopwords

# nltk.download()

text = 'This is my first sentens. That I\'m going to be tokenizing. Mr. Piotr will be one of the best in the world and' \
       ' most likely one of the reachest on the planet. Thant\'s for sure.'
sentens_text = nltk.sent_tokenize(text)
token_text = nltk.word_tokenize(text)
stop_words = set(stopwords.words("english"))
text_nostop = []


text_nostop = [x for x in token_text if not x in stop_words]


print(nltk.word_tokenize(text))
print(text_nostop)

indx = [x+1 for x in range(100)]
print(indx)