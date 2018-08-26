import  os
import json
from tkinter import filedialog
from xml.dom import minidom
import Normalizer.Normalizer_Trash_removal as normalizer

#esse script junta todos os corpos de texto de uma pasta em um unico arquivo.


file_opt={}
path = input("path:")

filesList = [name for name in os.listdir(path) ]

allInfo = []
for file in filesList:
    
        mydoc = minidom.parse(path+"\\"+file)

        #le as informações
        try:
            mainText = mydoc.getElementsByTagName('mainText')[0].firstChild.data
        except:
            print ('no text.')
        orientation = mydoc.getElementsByTagName('orientation')[0].firstChild.data

        title = "";
        try:
            title = mydoc.getElementsByTagName('title')[0].firstChild.data
        except:
            print ('no title.')
        url = mydoc.getElementsByTagName('uri')[0].firstChild.data
        veracity = mydoc.getElementsByTagName('veracity')[0].firstChild.data

        #normaliza o label
        label = False
        if "false" in veracity and  "no factual" not in veracity:
            #normaliza  titulo e texto
            title = normalizer.normalization(title)
            title = normalizer.tokenize_info(title)
            title = normalizer.stripNonAlphaNum(title)

            mainText = normalizer.normalization(mainText)
            mainText = normalizer.tokenize_info(mainText)
            mainText = normalizer.stripNonAlphaNum(mainText)

            data = {'title': title, 'orientation': orientation, 'text': mainText, 'url': url, 'label':label}
            print(data)
            allInfo.append(data)



name_arq = filedialog.asksaveasfilename(**file_opt)
arq = open(name_arq,'w')
data = allInfo
json.dump(data,arq)
arq.close()



# #esse script junta todos os corpos de texto de uma pasta em um unico arquivo.
# file_opt={}
# path = input("path:")
#
# filesList = [name for name in os.listdir(path) ]
#
# allInfo = ""
# for file in filesList:
#     try:
#         data_json = open(path+"\\"+file).read()
#         data_jsonInfo = json.loads(data_json)
#         info= data_jsonInfo.get('meta_data').get('og').get('description')
#         allInfo = allInfo + str(info)
#     except (RuntimeError,ValueError,TypeError, NameError, AttributeError):
#         try:
#             info = data_jsonInfo.get('text')
#             allInfo = allInfo + str(info)
#         except:
#             print("eita",file)
# name_arq = filedialog.asksaveasfilename(**file_opt)
# arq = open(name_arq,'w')
# data = allInfo
# json.dump(data,arq)
# arq.close()