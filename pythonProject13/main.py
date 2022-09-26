"""user = input("greeting:")
print('hello, viivi')"""

"""first = -9
second = 12_456_123_180
third = 4.973
fourth = -4 + 2j

print(first)
print(second)
print(third)
print(fourth)
print(fourth.real)
print(fourth.imag)"""
"""fahrenheit_str = input("Enter a temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit-32)*5/9
print("The temperature in Celsius: " + str(celsius))"""
"""birth_year = input("what is your birth year? ")
age = 2022 - int(birth_year)
print(age)"""
"""x = 10
x = x + 3
print(x)"""
"""x = 10 + 3 * 2
print(x)"""
"""price = 25
print(price > 10 and price < 30)"""
"""Temperature = 25
if Temperature > 30:
    print("It's a hot day")
    print("Drink lots of water")
elif Temperature > 20:
    print("It's a nice day")
elif Temperature > 10:
    print("it's bit cold")
else:
    print("It's cold")"""
"""i = 1
while i <= 5:
    print(i)
    i = i + 1"""
"""i = 1
while i <= 25:
    print(i)
    i = i + 5"""
"""money = float(input("Enter amount of money: "))
if money>=5:
    print("You can buy a latte.")
else:
    print('buy now')"""
"""cat = input("Enter the name of your cat: ")
dog = input("Enter the name of your dog: ")
if cat == dog:
    print("oh my! The cat and dog have same name")"""

"""age = int(input("Enter age: "))
if 15 <= age < 18:
    weight = float(input("Enter weight (kg): "))
if (age >=18 or age>=15 and weight >=55):
    print("The medicine can be used. ")
else:
    print("sorry, you cannot use")"""
"""age = int(input("Enter age: "))
if age>=65:
    print(" you are retired")
elif age>=18:
    print("you are working class")
elif age>=7:
    print("you are still child")"""
"""born_year = int(input("Enter your born year: "))
age = 2022-born_year
if age >= 18:
    print("oh yaa, you are eligible")
if age < 18:
    print("sorry, you are not eligible")
if age == 0:
    print("you are not human-being, are you?")
print("Thank you !")"""
"""born_year = int(input("Enter your born year: "))
age = 2022-born_year
if age >= 18:
    print("oh yah, you are eligible!")
else:
    print("sorry, you are not eligible")"""

"""password = "autum2022"
input_password = str(input("please enter your password: "))
if input_password == password:
    print("welcome!")
else:
    print("This password is incorrect")"""
"""postol_code = '28400'
city = "Tampere"
print(type(postol_code))
print(type(city))"""
"""born_year = int(input(" enter born year: "))
age = 2022-born_year
if age >= 18:
    print("oh yah! you are eligible")
elif 0 < age < 18:
    print("you are not eligible")
else:
    print(f"are you sure you were born in {born_year}?")
print("Thank you")"""
"""gender = input("Are you male or female? ")
hemoValue = float(input("Input your hemoglobin value (g/l): "))
if gender == "male":
    if hemoValue < 134:
        print("Your hemoglobin value is low")
    elif hemoValue > 167:
        print("Your hemoglobin value is high")
    else:
        print("Your hemoglobin value is normal")
else:
    if hemoValue < 117:
        print("Your hemoglobin value is low")
    elif hemoValue > 155:
        print("Your hemoglobin value is high")
    else:
        print("Your hemoglobin value is normal")"""
import random
# a 3-digit code where each number is between 0 and 9.
"""digit01 = str(random.randint(0,9))
digit02 = str(random.randint(0,9))
digit03 = str(random.randint(0,9))
print("A 3-digit code where each number is between 0 and 9: " + digit01 + digit02 + digit03)

# a 4-digit code where each number is between 1 and 6
digit01 = str(random.randint(1,6))
digit02 = str(random.randint(1,6))
digit03 = str(random.randint(1,6))
digit04 = str(random.randint(1,6))
print("A 4-digit code where each number is between 1 and 6: " + digit01 + digit02 + digit03 + digit04)"""

"""n = 3
while n <= 1000:
    if n % 3 == 0:
        print(n)
    n += 3"""
"""getInput = input("Input any number (negative number to exit): ")
numIn = float(getInput)
while numIn >= 0:
    numCm = numIn * 2.54
    print(getInput, "in =", numCm, "cm")
    getInput = input("Input any number (negative number to exit): ")
    numIn = float(getInput)"""
"""import random
ranNum = random.randint(1,10)
numGuess = int(input("Guess the number from 1-10: "))
while numGuess != ranNum:
    if numGuess < ranNum:
        print("Too low. Try again")
    else:
        print("Too high. Try again")
    numGuess = int(input("Guess the number from 1-10: "))
print("Correct!")"""
userOK = "python"
passOK = "rules"
username = input("Username: ")
password = input("Password: ")
time = 1
while (username != userOK or password != passOK) and time < 5:
    print("Login failed. Try again")
    username = input("Username: ")
    password = input("Password: ")
    time += 1
if username != userOK or password != passOK:
    print("Access denied")
else:
    print("Welcome")