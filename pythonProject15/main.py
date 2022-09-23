import mysql.connector

connection = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='root',
        password='root',
        autocommit=True
        )
def getflight_game(icao):
    sql = "select name from airport"
    sql += ' where ident="' + icao + '"'
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    return

getflight_game('00AA')