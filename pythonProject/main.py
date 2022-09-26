#Excercise 7
#1
"""season = ("Spring", "Summer", "Autumn", "Winter")
month = ([3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 1, 2])
inputNum = int(input("Input a month in number (1..12:) "))
for i in range(len(month)):
    if inputNum in month[i]:
        print(season[i])
        break"""
#2
"""nameSet = set()
tmpList = []
print("Input 5 names, please!")
i = 1
while i <= 5:
    nameInput = input(f"Name {i}: ")
    if nameInput not in nameSet:
        tmpList.append(nameInput)
        nameSet.update(tmpList)
        print("New name")
        i += 1
    else:
        print("Existing name")
for i in nameSet:
    print(i)"""
#3
"""dashboard = {}
def askingInfo():
    print("Choose what you want to do:")
    print("n: add new airport")
    print("f: fetch airport name")
    print("ENTER to quit program")
    return input()

query = askingInfo()
while query == "n" or query == "f":
    if query == "n":
        newIcao = input("input ICAO code: ")
        newName = input("input name of airport: ")
        dashboard.update({newIcao: newName})
    else:
        icao = input("input ICAO code: ")
        if icao in dashboard:
            print("Airport name:", dashboard[icao])
        else:
            print("Airport not found")
    query = askingInfo()
print("Thank you! Bye!")"""
#excercise 8
from tabulate import tabulate
import mysql.connector
testDB = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit= True

"""icao = input("Please input ICAO code: ")
mycursor = testDB.cursor()
mycursor.execute(f"select name as 'airport name', municipality as 'location' from airport where ident = '{icao}';")
result = mycursor.fetchall()
print(tabulate(result, tablefmt="fancy_grid"))
print(mycursor.rowcount, 'rows in set')"""

