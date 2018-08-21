import json
import requests
from tkinter import filedialog
from urllib.parse import urlparse


def analizesSource(fileData):

    # pega somente a URL so aquivo JSON
    urlFull = (json.loads(fileData)).get("url")

    # copia a URL completa para a var url para ser tratada
    url = urlFull

    # divide a URL em partes ex.:(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
    #                               params='', query='', fragment='')
    o = urlparse(url)

    # concatena apenas as partes interessantes da URL completa
    url = '{uri.scheme}://{uri.netloc}/'.format(uri=o)

    # URl's
    print('\n')
    print("======================================INICIO ANALISE DA FONTE======================================")
    print('\n')
    print('==================URL PARAMETRIZADA==================')
    print (url)
    print('\n')
    print('==================URL FULL==================')
    print (urlFull)
    print('\n')

    # Corpo da requisição GET
    payload = {'hosts': url, 'callback': 'process', 'key' : '4175cd3b4e4e52fb19c4037aa6f776ba60b175c6'}
    payloadFull = {'hosts': urlFull, 'callback': 'process', 'key' : '4175cd3b4e4e52fb19c4037aa6f776ba60b175c6'}

    # requisição GET
    res = requests.get(' http://api.mywot.com/0.4/public_link_json2', params = payload)
    resFull = requests.get(' http://api.mywot.com/0.4/public_link_json2', params = payloadFull)

    #retorna a resposta da requisição
    print('==================Retorno da Requisição da URL PARAMETRIZADA==================')
    print (res.text) 
    print('\n')
    print('==================Retorno da Requisição da URL COMPLETA==================')
    print (resFull.text) 
    print('\n')
    print("======================================FIM ANALISE DA FONTE======================================")
    print('\n') 



# inputPath = filedialog.askopenfilename()
# data_json = open(inputPath).read()

# analisesSource(data_json)