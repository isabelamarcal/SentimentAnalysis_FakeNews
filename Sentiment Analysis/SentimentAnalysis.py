# -*- coding: utf-8 -*-
"""
Análise de sentimento
TRABALHO DE CONCLUSÃO DE CURSO - 2 sem. 2018.
"Análise da influência de Atributos de Sentimento na Identificação de Fake News"
"""
import re
import unicodedata
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Analisa o sentimento do parágrafo inteiro e retorna um valor numérico representando o sentimento
def sentiment_value_per_paragraph(paragraph):
    analyser = SentimentIntensityAnalyzer()
    result = analyser.polarity_scores(paragraph)
    score = result['compound']
    return round(score,1)

    """
    [ -1, -0.5) : 1, V.Negative
    [-0.5, 0) : 2, Negative
    [0] : 3, Neutral
    (0, 0.5) : 4, Positive
    [0.5, 1] : 5, V.Positive
    [] inclusive
    () exclusive
    """

# Analisa o sentimento de cada frase do parágrafo e retorna as médias dos valores de sentimento de cada frase
def sentiment_value_per_phrase(paragraph):
    analyser = SentimentIntensityAnalyzer()
    text = nltk.sent_tokenize(paragraph)
    score = 0
    for phrase in text:
        result = analyser.polarity_scores(phrase)
        score = score + result['compound']
        print (phrase + " = " + str(result['compound']))
    score /= len(text)
    return round(score,1)

    """
    [ -1, -0.5) : 1, V.Negative
    [-0.5, 0) : 2, Negative
    [0] : 3, Neutral
    (0, 0.5) : 4, Positive
    [0.5, 1] : 5, V.Positive
    [] inclusive
    () exclusive
    """

# Parágrafo usado como exemplo 
sample = "I loved this one. But I didn't like that one."

print(sample)
sent = sentiment_value_per_paragraph(sample)
print('Sentiment paragraph: ' + str(sent))
sent = sentiment_value_per_phrase(sample)
print('Sentiment phrase: ' + str(sent))

