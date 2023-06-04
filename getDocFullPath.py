import mysql.connector
import os

basePath = "D:/Documentos Câmara/Arquivo da Câmara de Viçosa/"

sql = "INSERT INTO documentspath (documentId, path) VALUES (%s, %s)"


def readDirectory(dir, parentDir=None):
    fullDir = parentDir + "\\" + dir
    if os.path.isdir(fullDir):
        for file in os.listdir(fullDir):
            readDirectory(file, fullDir)
    else:
        return fullDir
    return None


# Conexão com o banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lampeh2004",
    database="arquivoscamara",
    port="3306"
)

# Criação do cursor para executar as consultas SQL
mycursor = mydb.cursor()

# Consulta SQL para selecionar todas as linhas da tabela 'minha_tabela'
sql = "SELECT * FROM documentos"

# Execução da consulta SQL
mycursor.execute(sql)

# Leitura dos resultados da consulta SQL
result = mycursor.fetchall()

# Exibição dos resultados
for row in result:
    if (row[-3] == None):
        continue
    splitPath = row[-3].split("/")[-2]
    if ("LocalizaÃ§Ã£o" in splitPath):
        splitPath = splitPath.replace("LocalizaÃ§Ã£o", "Localização")
    print("ID: ", row[0])
    print("Path: ", splitPath)
    print("\n")

    # verify files in path
    try:
        for infile in os.listdir(basePath + splitPath):
            fullDir = readDirectory(infile, splitPath)
            if (fullDir != None):
                print(fullDir)
                # mycursor.execute(sql, (row[0], fullDir))
                # mydb.commit()
    except:
        print("Path not found")
        print("-----------------")
    # if("99.99.102" in splitPath):
    #   break
    print("------------------")

# Fechamento da conexão com o banco de dados
mydb.close()
