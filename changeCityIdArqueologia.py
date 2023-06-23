import mysql.connector


def get_properties_names(obj):
    classname = obj.__class__
    components = dir(classname)
    properties = filter(lambda attr: type(getattr(classname, attr)) is property, components)
    return properties


#
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
        print("Conexão com o banco de dados realizada com sucesso!")
except mysql.connector.Error as error:
    print("Falha na conexão com o banco de dados: {}".format(error))

# # Criação do cursor para executar as consultas SQL
mycursor = mydb.cursor()

dadoscidade = [
    [405, 430],
    [432, 434],
    [438, 440],
    [443, 444],
    [448, 450],
    [452, 453],
    [455, 456],
    [459, 461],
    [463, 464],
    [467, 468],
    [471, 472],
    [475, 477],
    [479, 480],
    [482, 483],
    [486, 487],
    [490, 491],
    [494, 495],
    [498, 499],
    [501, 502],
    [504, 505],
    [507, 508],
    [510, 512],
    [516, 517],
    [521, 522],
    [526, 528],
    [533, 534],
]
historicoibge = [
    571,
    582,
    590,
    600,
    603,
    606,
    609,
    612,
    619,
    621,
    623,
    626,
    629,
    630,
    631,
    632,
    633,
    634,
    635,
    636,
    637,
    638,
    639,
    640,
    641,
    642,
]

for i, row in enumerate(dadoscidade):
    print('dadoscidade')
    print(i, row)
    print('\n')
    alterRowTypeSql = "UPDATE dadoscidades SET cityId = %s WHERE cityId = %s OR cityId = %s"
    mycursor.execute(alterRowTypeSql, (i+1, row[0],row[1]))
    mydb.commit()
for i, row in enumerate(historicoibge):
    print('historicoibge')
    print(i, row)
    print('\n')
    alterRowTypeSql = "UPDATE historicoibge SET cityId = %s WHERE cityId = %s"
    mycursor.execute(alterRowTypeSql, (i + 1, row))
    mydb.commit()
