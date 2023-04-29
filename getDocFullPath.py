import mysql.connector
import os

basePath = "C:\\Users\\gabri\\Documents\\GitHub\\arquivoscamara\\arquivos\\"


def readDirectory(dir, parentDir=None):
    fullDir = parentDir + "\\" + dir
    if os.path.isdir(fullDir):
        for file in os.listdir(fullDir):
            readDirectory(file, fullDir)
    else:
        print(fullDir)


# Conexão com o banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
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
sql = "INSERT INTO documentspath (documentId, path) VALUES (%s, %s)"
# Exibição dos resultados
for row in result:
    print("ID: ", row[0])
    print("Path: ", row[-3])
    print("\n")
    # verify files in path
    for infile in os.listdir(basePath + row[-3]):
        readDirectory(infile, basePath + row[-3])
        print("-----------------")

# Fechamento da conexão com o banco de dados
mydb.close()
