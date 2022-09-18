"""def greet(first_name, last_name):
    print(f"Hi{first_name}, {last_name}")
    print("Welcome aboard")


greet("Bishwa", "Ghimire")
greet("John", "Sina")"""

"""born_year = int(input("Enter your year of birth:"))
age = 2022-born_year
if age >= 18:
    print("oh yeah, you are eligible")
if age < 18:
    print("sorry, you are not eligible")
if age == 0:
    print("you are not human-being, you are?")
print("thank you!")"""
"""born_year = int(input("Enter year of your birth:"))
age = 2022-born_year
if age >= 18:
    print("oh yeah! you are eligible")
else:
    print("sorry, you are not eligible")"""
"""password = "bishwa2022"
input_password = str(input("Please enter your password:"))
if input_password == password:
    print("welcome!")
else:
    print("password is incorrect")"""
"""born_year = int(input("Enter your year of birth:"))
age = 2022-born_year
if age >= 18:
    print("oh yeah, you are eligible")
elif 0 < age < 18:
    print("you are not eligible")
else:
    print(f"Are you sure you were born in {born_year}?")
print("Thank you")"""
"""greetings = int(input("How many do you want to display?"))
first_greeting = 0
while first_greeting < greetings:
    print("Good morning")
    first_greeting = first_greeting + 1"""
"""command = input("Enter command:")
while command != "stop":
    print("Executing command:")
    command = input("Enter command:")
print("Execution is stopped")"""
"""import random
dice1 = dice2 = rolls = 0
while (dice1 != 6 or dice2 !=6):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    rolls +=1
print(f"dice was rolled {rolls:d} times.")"""

"""first = 1
while first <= 5:
    second = 1
    while second <= 5:
        print(f"{first} times {second} is {first*second:d}")
        second = second + 1
    first = first + 1"""
"""command = input ("Enter command: ")
while command!="stop":
    if command=="MAYDAY":
        break
    print("Execution command: " + command)
    command = input("Enter command: ")
print ("Execution is stopped.")"""
list1 = []
match_points = [9, 4, 3, 8, 10, 6]
print(match_points[0])
print(match_points[3])
print(match_points[5])
print("The total points of these matches is:", match_points[0] + match_points[3] + match_points[5])







