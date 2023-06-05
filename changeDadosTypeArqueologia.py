import mysql.connector
import json

libraryItems = ['430', '434', '440', '444', '450', '453', '456', '461', '464', '468', '472', '477', '480', '483', '487',
                '491', '495', '499', '502', '505', '508', '512', '517', '522', '528', '534']

# Conexão com o banco de dados
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="arqueologia",
        port="3306"
    )
    if mydb.is_connected():
        print("Conexão com o banco de dados local realizada com sucesso!")
except mysql.connector.Error as error:
    print("Falha na conexão com o banco de dados: {}".format(error))

# # Criação do cursor para executar as consultas SQL
mycursor = mydb.cursor()
# # Consulta SQL para selecionar todas as linhas da tabela 'minha_tabela'
sql = "SELECT * FROM dadoscidades"
mycursor.execute(sql)
#
# # Leitura dos resultados da consulta SQL
result = mycursor.fetchall()
# # Exibição dos resultados
for row in result:
    # print("ID: ", row[7])
    if row[7] in libraryItems:
        alterRowTypeSql = "UPDATE dadoscidades SET type = 'library' WHERE id = %s"
    else:
        alterRowTypeSql = "UPDATE dadoscidades SET type = 'archive' WHERE id = %s"
    mycursor.execute(alterRowTypeSql, (row[0],))
    mydb.commit()

mydb.close()
