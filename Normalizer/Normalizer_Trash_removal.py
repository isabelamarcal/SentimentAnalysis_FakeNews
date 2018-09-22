# -*- coding: utf-8 -*-
"""
Spyder Editor

Normalização de textos para Processamento de Linguagem Natural
TRABALHO DE CONCLUSÃO DE CURSO - 2 sem. 2018.
"Análise da influência de Atributos de Sentimento na Identificação de Fake News"
"""
import json
import re
import unicodedata
import tkinter as tk
from tkinter import filedialog
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')

file_opt={}

#Tokenização do campo "informação", removendo stopwords
def tokenize_info(info):
    
    stopWords = set(stopwords.words('english'))
    words = word_tokenize(info)
    wordsFiltered = []
    
    for w in words:
        if w not in stopWords:
            if w == "nt":
                w = "not" ;
            wordsFiltered.append(w)
            
    info_tokenized = ""
    
    for w in words:
        if w not in stopWords:
            info_tokenized = info_tokenized + " " + w
    
    return info_tokenized

#Criação do arquivo Json filtrado e normalizado
def create_normalized_Json(title,author,info_tokenized,url):
    
    name_arq = filedialog.asksaveasfilename(**file_opt)
    arq = open(name_arq,'w')
    data = {'title':title,'author':author,'information':info_tokenized,'url':url}
    json.dump(data,arq) 
    arq.close()
    return 

#Remoção de caracteres não alfanuméricos
def stripNonAlphaNum(information):

    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', information)
    stripedWord = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', stripedWord)

#Normaliza o campo "Description" do arquivo, retirando maiúsculas 
def normalization(information):
    
    return information.lower()

#Faz a leitura do Json no padrão do Dataset "https://github.com/KaiDMML/FakeNewsNet"
def read_Json():
    
    root = tk.Tk()
    root.withdraw()

    inputPath = filedialog.askopenfilename()
    data_json = open(inputPath).read()
    data_jsonInfo = json.loads(data_json)
    
    title = data_jsonInfo.get('meta_data').get('og').get('title')
    author = data_jsonInfo.get('authors')
    author = str(author).replace('[','')
    author = str(author).replace(']','')
    info = data_jsonInfo.get('meta_data').get('og').get('description')
    url = data_jsonInfo.get('meta_data').get('og').get('url')
    
    info = normalization(info)
    info = stripNonAlphaNum(info)    

    info_tokenized = tokenize_info(info)

    create_normalized_Json(title,author,info_tokenized,url)
    
    print('Title: ',title)
    print('Author name: ',author)
    print('Information: ',info_tokenized)
    print('Url: ',url)

"""
Informations:
    authors
    meta-data/og/title
    meta-data/og/description     <- Normalize!
    meta-data/og/url
"""

"""
{‘ourselves’, ‘hers’, ‘between’, ‘yourself’, ‘but’, ‘again’, ‘there’, ‘about’, 
‘once’, ‘during’, ‘out’, ‘very’, ‘having’, ‘with’, ‘they’, ‘own’, ‘an’, ‘be’, 
‘some’, ‘for’, ‘do’, ‘its’, ‘yours’, ‘such’, ‘into’, ‘of’, ‘most’, ‘itself’, 
‘other’, ‘off’, ‘is’, ‘s’, ‘am’, ‘or’, ‘who’, ‘as’, ‘from’, ‘him’, ‘each’, 
‘the’, ‘themselves’, ‘until’, ‘below’, ‘are’, ‘we’, ‘these’, ‘your’, ‘his’, 
‘through’, ‘don’, ‘nor’, ‘me’, ‘were’, ‘her’, ‘more’, ‘himself’, ‘this’, ‘down’
, ‘should’, ‘our’, ‘their’, ‘while’, ‘above’, ‘both’, ‘up’, ‘to’, ‘ours’, 
‘had’, ‘she’, ‘all’, ‘no’, ‘when’, ‘at’, ‘any’, ‘before’, ‘them’, ‘same’, 
‘and’, ‘been’, ‘have’, ‘in’, ‘will’, ‘on’, ‘does’, ‘yourselves’, ‘then’, ‘that’
, ‘because’, ‘what’, ‘over’, ‘why’, ‘so’, ‘can’, ‘did’, ‘not’, ‘now’, ‘under’, 
‘he’, ‘you’, ‘herself’, ‘has’, ‘just’, ‘where’, ‘too’, ‘only’, ‘myself’, 
‘which’, ‘those’, ‘i’, ‘after’, ‘few’, ‘whom’, ‘t’, ‘being’, ‘if’, ‘theirs’, 
‘my’, ‘against’, ‘a’, ‘by’, ‘doing’, ‘it’, ‘how’, ‘further’, ‘was’, ‘here’, 
‘than’}
"""

# lemos o JSON em disco
#Main function

#read_Json()
    
        
        
