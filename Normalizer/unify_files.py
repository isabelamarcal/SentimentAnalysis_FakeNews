import  os
import json
from tkinter import filedialog

#esse script junta todos os corpos de texto de uma pasta em um unico arquivo.
file_opt={}
path = input("path:")

filesList = [name for name in os.listdir(path) ]

allInfo = ""
for file in filesList:
    try:
        data_json = open(path+"\\"+file).read()
        data_jsonInfo = json.loads(data_json)
        info= data_jsonInfo.get('meta_data').get('og').get('description')
        allInfo = allInfo + str(info)
    except (RuntimeError,ValueError,TypeError, NameError, AttributeError):
        try:
            info = data_jsonInfo.get('text')
            allInfo = allInfo + str(info)
        except:
            print("eita",file)
name_arq = filedialog.asksaveasfilename(**file_opt)
arq = open(name_arq,'w')
data = allInfo
json.dump(data,arq)
arq.close()