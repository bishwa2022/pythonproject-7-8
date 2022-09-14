"""import random
numDice = int(input("How many dice to roll? "))
sumRoll = 0
for i in range (numDice):
    sumRoll += random.randint(1,6)
print("Sum of all dices is: ", sumRoll)"""

# phase 2
"""print("Please input at least 5 numbers !!!")
listNum = []
num = input("Input a number: ")
while num != "":
    listNum.append(int(num))
    num = input("Input a number: ")
listNum.sort(reverse=True)
print("The first 5 greatest numbers are:")
for i in range (5):
    print(listNum[i], end="   ")"""

#phase 3
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

# phase 4
"""listCity = []
print("Please input name of 5 cities")
for i in range(5):
    listCity.append(input("Name of a city: "))
for i in range(5):
    print(listCity[i])"""
#phase 5
"""import random
def diceRoll():
    return random.randint(1,6)
num = diceRoll()
while num != 6:
    print(num)
    num = diceRoll()
print(num)"""
#phase 6
import random
def diceRoll(sides):
    return random.randint(1,sides)
numSides = int(input("How many sides the dice has? "))
num = diceRoll(numSides)
while num != numSides:
    print(num)
    num = diceRoll(numSides)
print(numSides)

