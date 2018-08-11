from nltk.tokenize import word_tokenize
import nltk
from nltk.metrics.spearman import *
from nltk.collocations import *
nltk.download('punkt')
#from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP

text = "claims democratic candidate " \
       " governor matt  turned flynn told one child predator " \
       " wait see turned authorities"

tokens = word_tokenize(text)
freq = nltk.FreqDist(tokens)
freq.plot(2)
sortDict = sorted(freq, key=lambda x: (-freq[x], x))

#não - direcionado
print('Não-Direcionado:')
for key in sortDict:
    print(key, freq[key])

#comprimento medio palavras

print('Cumprimento medio das palavras:')
mediumLen = text.replace(" ","").__len__()/tokens.__len__()
print(mediumLen)








