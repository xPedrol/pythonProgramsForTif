import mysql.connector
import json


def get_properties_names(obj):
    classname = obj.__class__
    components = dir(classname)
    properties = filter(lambda attr: type(getattr(classname, attr)) is property, components)
    return properties


#
# Conexão com o banco de dados
libraryItems = ['430', '434', '440', '444', '450', '453', '456', '461', '464', '468', '472', '477', '480', '483', '487',
                '491', '495', '499', '502', '505', '508', '512', '517', '522', '528', '534']
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="arqueologia",
        port="3306"
    )
    if mydb.is_connected():
        print("Conexão com o banco de dados realizada com sucesso!")
except mysql.connector.Error as error:
    print("Falha na conexão com o banco de dados: {}".format(error))
# # verify connection
#
#
mydb2 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="arqueologia_db",
    port="3306"
)
#
# # Criação do cursor para executar as consultas SQL
mycursor = mydb.cursor()
#
mycursor2 = mydb2.cursor()
#
# # Consulta SQL para selecionar todas as linhas da tabela 'minha_tabela'
sql = "SELECT * FROM wp_ninja_table_items"
#
# # Execução da consulta SQL
# mycursor2.execute(sql)
# #
# # # Leitura dos resultados da consulta SQL
# result = mycursor2.fetchall()
# # sql = "INSERT INTO dadoscidades (title,year,subject,comments,link,material,cityId,author) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
# # # Exibição dos resultados
# for row in result:
#     print("ID: ", row[7])
#     if row[7] in [430, 405]:
#         alterRowTypeSql = "UPDATE dadoscidades SET cityId = 1 WHERE cityId = %s"
#         mycursor.execute(alterRowTypeSql, (row[7],))
#         mydb.commit()
#     if(row[7] in [571]):
#         alterRowTypeSql = "UPDATE historicoibge SET cityId = 1 WHERE cityId = %s"
#         mycursor.execute(alterRowTypeSql, (row[7],))
#         mydb.commit()
for row in [448, 450]:
    alterRowTypeSql = "UPDATE dadoscidades SET cityId = 1 WHERE cityId = %s"
    mycursor.execute(alterRowTypeSql, (row,))
    mydb.commit()
for row in [603]:
    alterRowTypeSql = "UPDATE historicoibge SET cityId = 1 WHERE cityId = %s"
    mycursor.execute(alterRowTypeSql, (row,))
    mydb.commit()
