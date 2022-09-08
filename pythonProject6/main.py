import random
import math

n = 1
while n <= 1000:
    if n % 3 == 0:
        print(n)
    n = n + 1

# phase 2

"""prompt = ("Give me inches?")
inch = float(input(prompt))
while inch >= 0:
    print(f"it is in centimeter: {inch*2.54:.if}:")
    inch = float(input(prompt)"""

# phase 3

"""prompt = "Give me a number"
s = input(prompt)
smallest = int(s)
largest = smallest
while s != "":
    n = int(5)
    if n < smallest:
        smallest = n
    else: n > largest
        largest = n
    5 = input(prompt)
else:
    print(f"The smallest given was {smallest}, and largest was {largest}")"""

# phase 4

"""the_number = random.randint(1, 10)
prompt = "Try to guess the number?"
guess = int(input(prompt))
while guess != the_number:
    if guess > the_number:
        print("Too high")
    else:
        print("Too low")
    guess = int(input(prompt))
else:
    print("Correct")"""

"""username = "python"
password = "rules"
n = 5
while n > 0:
    u = input("Give the username?")
    p = input("Give the password?")
    if u == username and p == password:
        print("Welcome")
        break
    n = n - 1
else:
    print("Access denied")"""

"""N = int(input("How many random points to generate?"))
n = 0
i = 0
while N > i:
    x = random.uniform(-1., 1.)
    y = random.uniform(-1., 1.)

    if x**2 + y**2 < 1.:
        n = n + 1
    i += 1
pi = 4.*n/N
print(f"pi is {pi}, error {math.pi - pi}")"""
"""n = 1
while n <= 7:
    print(f"{n}")
    n = n + 0
print("1")
print("2")
print("3")
print("4")
print("5")
print("6")
print("7")"""


"""def hello():
    print("Hello World")
    for i in range(5):
        print("-----------")
    print("Good bye World")
    return"""


"""def minus(argument):
    if argument > 0:
        return -argument
    else:
        return argument


def sqr(a):
    x = a / 2  # initial guess for the square root

    while abs(x * x - a) >= 0.001:  # Iterative algorithm until we have enough accuracy
        x = (a / x * X) / 2  # improve the estimate x for the square root

    return x


def plus(a, b):
    return a + b


result = plus(2, 6)
print(f"{result}")"""


