import random
numDice = int(input("How many dice to roll? "))
sumRoll = 0
for i in range (numDice):
    sumRoll += random.randint(1,6)
print("Sum of all dices is: ", sumRoll)

print("Please input at least 5 numbers !!!")
listNum = []
num = input("Input a number: ")
while num != "":
    listNum.append(int(num))
    num = input("Input a number: ")
listNum.sort(reverse=True)
print("The first 5 greatest numbers are:")
for i in range (5):
    print(listNum[i], end="   ")

num = int(input("Input an integer number: "))
halfNum = num // 2
divisible = False
for i in range (2, halfNum+1):
    if num % i == 0:
        divisible = True
        break
if divisible == False:
    print("This is a prime number")
else:
    print("This is not a prime number")
listCity = []
print("Please input name of 5 cities")
for i in range(5):
    listCity.append(input("Name of a city: "))
for i in range(5):
    print(listCity[i])

import random
def diceRoll():
    return random.randint(1,6)
num = diceRoll()
while num != 6:
    print(num)
    num = diceRoll()
print(num)

import random
def diceRoll(sides):
    return random.randint(1,sides)
numSides = int(input("How many sides the dice has? "))
num = diceRoll(numSides)
while num != numSides:
    print(num)
    num = diceRoll(numSides)
print(numSides)

def gallonToLit(gallons):
    return gallons * 3.785
print("Input negative number to exit")
numGallon = float(input("How many gallons? "))
while numGallon >= 0:
    print(f"Equal to {gallonToLit(numGallon):.4f} litters")
    numGallon = float(input("How many gallons? "))
def sumList(intList):
    sumResult = 0
    for i in intList:
        sumResult += i
    return sumResult
predefList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sum of a list is: ",sumList(predefList))
def showList(intList):
    newList = []
    for i in intList:
        if i % 2 == 0:
            newList.append(i)
    print("Old list: ", intList)
    print("New list: ", newList)
predefList = [1,2,3,4,5,6,7,8,9,10]
showList(predefList)
import math
def calcPricePizza(diameter, price,name):
    areaPizza = math.pi * diameter * diameter
    print("The price per square meter of pizza",name,f": {price / (areaPizza * 0.0001):.3f}")
    return price / (areaPizza * 0.0001)
dia1 = float(input("Input the diameter of pizza 1 in cm: "))
price1 = float(input("Input the price of pizza 1 in euro: "))
dia2 = float(input("Input the diameter of pizza 2 in cm: "))
price2 = float(input("Input the price of pizza 2 in euro: "))
if calcPricePizza(dia1,price1,1) < calcPricePizza(dia2,price2,2):
    print("Pizza 1 is cheaper than pizza 2")
elif calcPricePizza(dia1,price1,1) > calcPricePizza(dia2,price2,2):
    print("Pizza 2 is cheaper than pizza 1")
else:
    print("Same price")

