import os
import shutil

from time import sleep
from selenium import webdriver
directory = input("Caminho do diretório:")
#directory = 'E:/Pedro - 2o Oficio -  lançamentos 2022/2o Oficio Lançamento outubro 2022/1785 CODICE 54 AUTO 1231-REVISADO'
def convertFolder(folderName):
    quantidadeDoc = os.listdir(folderName)
    novoA = directory.replace('REVISADO','CONCLUIDO')
    
    if not os.path.exists(novoA):
        os.mkdir(novoA)#creates final folder
    if not os.path.exists('CONC'):
        os.mkdir('CONC')#creates final folder
    os.chdir(directory)
    cont=0
    for x in quantidadeDoc:
        cont=cont+1
        print("Imagem: ", (cont))
        os.system('vips.exe tiffsave '+folderName+'/'+x+'  CONC/'+x+' --compression=jpeg --Q=75 --tile --tile-width=256 --tile-height=256 --pyramid')
    # os.chdir('D:/1781-1810/1861 - 1870 Lancamentos 2020 Concluidos2')
    os.chdir(directory)

#print(os.getcwd())SSZZ
# os.chdir('D:/1781-1810/1861 - 1870 Lancamentos 2020 Concluidos2')
os.chdir(directory)
folder = os.listdir()

for name in folder:
    if os.path.isdir(name) and name=='CONV':
        print("Convertendo: "+name)
        convertFolder(name)