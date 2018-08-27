import json
import requests
from tkinter import filedialog
from urllib.parse import urlparse


def analizeSource(data):

    # pega somente a URL so aquivo JSON
    # urlFull = (json.loads(data)).get("url")

    # copia a URL completa para a var url para ser tratada
    url = data

    # divide a URL em partes ex.:(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html', params='', query='', fragment='')
    o = urlparse(url)

    # concatena apenas as partes interessantes da URL completa
    url = '{uri.scheme}://{uri.netloc}/'.format(uri=o)

    target = '{uri.netloc}'.format(uri=o)

    # URl's
    # print('\n')
    # print("======================================ANALISE DA FONTE======================================")
    # print('\n')
    # print('==================URL==================')
    # print (url)
    # print('\n')

    # Corpo da requisição GET
    payload = {'hosts': url, 'callback': '', 'key' : '4175cd3b4e4e52fb19c4037aa6f776ba60b175c6'}

    # requisição GET
    res = requests.get(' http://api.mywot.com/0.4/public_link_json2', params = payload)

    #retorna a resposta da requisição
    # print('==================Retorno da Requisição da URL==================')
    # print('\n')
    # print (((json.loads((res.text.split("(")[1]).split(")")[0])).get(target)).get('0'))
    if ((json.loads((res.text.split("(")[1]).split(")")[0])).get(target)).get('0') :
        trustworthiness_1 = ((json.loads((res.text.split("(")[1]).split(")")[0])).get(target)).get('0')[0]
        trustworthiness_2 =((json.loads((res.text.split("(")[1]).split(")")[0])).get(target)).get('0')[1]
    else: 
        trustworthiness_1 = trustworthiness_2 = 0

    print("============================================================================")
    # print (res.text) 
    # print (trustworthiness_1)
    # print (trustworthiness_2) 
    if trustworthiness_1 < 50 :
        # if trustworthiness_2 < 50 :
            print('unreliable') 
    if trustworthiness_1 >= 50 :
        # if trustworthiness_2 > 50 :
            print('trustworthy') 
    # print("======================================FONTE======================================")
    # print('\n')



# inputPath = filedialog.askopenfilename()
# data_json = open(inputPath).read()

# analisesSource(data_json)