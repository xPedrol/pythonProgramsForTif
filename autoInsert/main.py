# coding=utf-8
import textract
import re
import os
import shutil


##trying to automate all the proccess
### Create a Document Class to improve it


def strData(text, line):
    variable = text[line].split(":")[1]
    variable = variable.split('\n')[0]
    variable = re.sub(r"^\s+", "", variable)
    return variable


def numberDatas(text, line):
    try:
        variable = re.findall(r'\d+', text[line])[0]
        return variable
    except:
        return 0


def move(source, URL):
    images = os.listdir(source)
    for img in images:
        shutil.move(source + '/' + img, URL)


def readText(ficha):
    oldText = textract.process(ficha)
    text = open("newtext.txt", mode="w+")
    a = oldText.decode('utf-8')
    ##save the content in a decent file
    text.write(a)
    text.close()


def getText():
    newfile = open("newtext.txt", mode="r")
    newtext = newfile.readlines()
    return newtext


def defineOficio(Oficio):
    if Oficio == "1":
        OficioURL = "Cartorio do Primeiro Oficio"
    else:
        OficioURL = "Cartorio do Segundo Oficio"
    return OficioURL


def defineURL(OficioURL, Ano, Codice, Auto):
    URL = "C:/inetpub/wwwroot/CasaSetecentista/Documentos/Arquivo da Casa Setecentista de Mariana/" + OficioURL + "/Inventarios/Ano " + Ano + "/Codice " + Codice + "/Auto " + Auto
    return URL


def insert(folderName):
    # os.chdir('D:/1751-1780/1751-1760 Lançamentos 2020 Concluidos2/'+folderName)
    ficha = os.listdir(folderName)[-1]
    # ALTERAR URL AQUI
    readText(directory + '/' +folderName + '/' + ficha)
    newtext = getText()
    numberData = re.findall(r'\d+', newtext[1])
    Codice = numberData[0]
    Auto = numberData[1]
    Oficio = numberData[2]

    Inventariante = strData(newtext, 3)
    Inventariado = strData(newtext, 4)

    if "Não Consta" in newtext[5] or "Não possui" in newtext[5] or "não consta" in newtext[5] or "Não consta" in \
            newtext[5] or "não possui" in newtext[5]:
        MonteMor = newtext[5].split(":")[1]
        MonteMor = MonteMor.split('\n')[0]
        MonteMor = re.sub(r"^\s+", "", MonteMor)
    else:
        if len(newtext[5].split(":")) > 2:
            MonteMor = newtext[5].split(":")[1] + ':' + newtext[5].split(":")[2]
            MonteMor = MonteMor.split('\n')[0]
            MonteMor = re.sub(r"^\s+", "", MonteMor)
        else:
            MonteMor = newtext[5].split(":")[1]
            MonteMor = MonteMor.split('\n')[0]
            MonteMor = re.sub(r"^\s+", "", MonteMor)

    Ano = numberDatas(newtext, 6)
    Local = strData(newtext, 7)

    NImagens = numberDatas(newtext, 8)
    OBS = strData(newtext, 9)

    # print(Inventariado)
    # print(Inventariante)
    # print(MonteMor)
    # print(Codice)
    # print(Auto)
    # print(Oficio)
    # print(Ano)
    # print(Local)
    # print(OBS)
    # print(NImagens)

    # Automate(Inventariado, Inventariante, MonteMor, Codice, Auto, Oficio, Ano, Local, NImagens, OBS)
    OficioURL = defineOficio(Oficio)
    # ALTERAR URL AQUI
    Source = directory +'/' + folderName
    URL = defineURL(OficioURL, Ano, Codice, Auto)
    print(Source)
    print(URL)
    # move(Source, URL)
    # os.rmdir(Source)


#################Starts here###############
# ALTERAR URL AQUI
directory = input('Digite o diretório')
# 'E:/Pedro - 2o Oficio -  lançamentos 2022/2o Oficio Lançamento outubro 2022'
os.chdir(directory)
folder = os.listdir()
i=1
for name in folder:
    if 'CONCLUIDO' in name:
        # auto = os.listdir(name)
        print("Inserindo: " + name)
        # print(auto[1])
        insert(name)
        print("---------------------------------------")
        i=i+1
print(f'Total de {i} documentos')
##progresssssssssss
