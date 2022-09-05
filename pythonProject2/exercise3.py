n = 1
while n <= 1000:
    if n%3 == 0:
        print(str(n))
    n = n + 1
zander = int(input("What is the size of zander in cm "))
if zander < 42:
    print("release fish because it is small", abs(zander - 42))
else:
    print("enjoy fishing")