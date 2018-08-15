import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import SnowballStemmer
from nltk.tokenize import PunktSentenceTokenizer

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def freqDist(text):
    sentences = nltk.sent_tokenize(text)
    for sent in sentences:
        print(nltk.pos_tag(nltk.word_tokenize(sent)))
    ps = SnowballStemmer("english")

    tokens = word_tokenize(text)
    tokens[:] = [ps.stem(word) for word in tokens]

    freq = nltk.FreqDist(tokens)
    return freq








