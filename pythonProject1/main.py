zander = int(input("What is the size of zander in cm "))
 if zander < 42:
     print("release fish because it is small", abs(zander - 42))
 else:
    print("enjoy fishing")

Cruiseship = input("What is the cabin class")
Lux = Cruiseship
if "Lux" == Lux:
  print("LUX: upper-deck cabin with a balcony")
elif "A" == Lux:
    print("A: above the car deck, equipped with a window")
elif "B" == Lux:
    print(print("B: windowless cabin above the car deck"))
elif "C" == Lux:
    print("C: windowless cabin below the car deck")

gender = input("Are you male of female? ")
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
        print("Your hemoglobin value is normal")



