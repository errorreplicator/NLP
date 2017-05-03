import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw("2005-GWBush.txt")

data = state_union.raw("2006-GWBush.txt")

tokenizer = PunktSentenceTokenizer()

tokenized = tokenizer.tokenize(data)
sentens_text = nltk.sent_tokenize(data)

# print(len(tokens))
# print(len(sentens_text))

for i in tokenized[:10]:
    words = nltk.word_tokenize(i)
    czesci_mowy = nltk.pos_tag(words)
    print(czesci_mowy)