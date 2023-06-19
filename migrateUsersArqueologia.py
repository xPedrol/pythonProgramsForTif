import random
import string

import mysql.connector
import json

#
# Conexão com o banco de dados
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="arqueologia",
        port="3306"
    )
    mydb2 = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="arqueologia_db",
        port="3306"
    )
    if mydb.is_connected():
        print("Conexão com o banco de dados novo realizada com sucesso!")
    if mydb2.is_connected():
        print("Conexão com o banco de dados novo realizada com sucesso!")
except mysql.connector.Error as error:
    print("Falha na conexão com o banco de dados: {}".format(error))

# # Criação do cursor para executar as consultas SQL
mycursor = mydb.cursor()
mycursor2 = mydb2.cursor()

sql = "SELECT * FROM `wp_users`"
mycursor2.execute(sql)
myresult = mycursor2.fetchall()
for row in myresult:
    login = row[1]
    socialName = row[9]
    email = row[1]
    password = row[2]
    createdAt = row[6]
    # generate token with 11 characters
    token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=11))
    sql = "INSERT INTO `usuarios` (`login`, `socialName`, `email`, `password`, `createdAt`,`token`) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (login, socialName, email, password, createdAt, token)
    mycursor.execute(sql, val)
    mydb.commit()
