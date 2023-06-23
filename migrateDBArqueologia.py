import mysql.connector
import json

# Conexão com o banco de dados
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="G21bxy.com",
        database="arqueologia",
        port="3306"
    )
    if mydb.is_connected():
        print("Conexão com o banco de dados local realizada com sucesso!")
except mysql.connector.Error as error:
    print("Falha na conexão com o banco de dados: {}".format(error))
# # verify connection
#
#
try:
    mydb2 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="G21bxy.com",
        database="arqueologia_db",
        port="3306"
    )
    if mydb2.is_connected():
        print("Conexão com o banco de dados wordpress realizada com sucesso!")
except mysql.connector.Error as error:
    print("Falha na conexão com o banco de dados: {}".format(error))
#
# # Criação do cursor para executar as consultas SQL
mycursor = mydb.cursor()
#
mycursor2 = mydb2.cursor()
#
# # Consulta SQL para selecionar todas as linhas da tabela 'minha_tabela'
sql2 = "SELECT * FROM wp_ninja_table_items"
#
# # Execução da consulta SQL
mycursor2.execute(sql2)
#
# # Leitura dos resultados da consulta SQL
result = mycursor2.fetchall()
# # Exibição dos resultados
for row in result:
    objeto = json.loads(row[6])
    tableId = row[2]
    if "historico" in objeto or "coluna_teste" in objeto:
        print("Table ID: ", row[2])
        print(objeto)
        print("\n")
        sql = "INSERT INTO historicoibge (description, cityId,url) VALUES (%s, %s,%s)"
        link = objeto["link"] if "link" in objeto else None
        description = objeto["historico"] if "historico" in objeto else objeto["coluna_teste"]
        mycursor.execute(sql, (description, tableId, link))
        mydb.commit()

    if "titulo" in objeto:
        ano = objeto["ano"] if "ano" in objeto else 0
        obs = objeto["observacoes"] if "observacoes" in objeto else None
        author = objeto["autor"] if "autor" in objeto else None
        link = objeto["link"] if "link" in objeto else None
        material = objeto["material"] if "material" in objeto else None
        assunto = objeto["assunto"] if "assunto" in objeto else None
        titulo = objeto["titulo"] if "titulo" in objeto else None
        sql = "INSERT INTO dadoscidades (title,year,subject,comments,link,material,cityId,author) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        mycursor.execute(sql, (titulo, ano, assunto, obs, link, material, int(row[2]), author))
        mydb.commit()
    # print(mycursor.rowcount, "linha(s) inserida(s).")
    # Fechamento da conexão com o banco de dados

mydb.close()
