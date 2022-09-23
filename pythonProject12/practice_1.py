"""fish_length = int(input("give me a size of Zinder:"))
if fish_length <= 41:
    print('relese zinder')
if fish_length >= 42:
    print('enjoy fishing')"""

"""cabin_class = input("give me the cabin class:")
if cabin_class == "LUX":
    print('upper-deck cabin with a balcony')
elif cabin_class == "A":
    print('above the car deck, equipped with a window')
elif cabin_class == "B":
    print('windowless cabin above the car deck')
elif cabin_class == "C":
    print('windowless cabin below the car deck')
else:
    print("invalid cabin class !!!")"""
"""user = input("What is the the biological gender and hemoglobin value:")
user1 = 'adult woman'
if hemoglobin_value == 'normal + user1 + 117-155'
user2 = 'adult man'"""
dashboard = {}
print("Choose what you want to do:")
print("n: add new airport")
print("f: fetch airport name")
print("ENTER to quit program")
query = input()
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
    print("Choose what you want to do:")
    print("n: add new airport")
    print("f: fetch airport name")
    print("ENTER to quit program")
    query = input()
print("Thank you! Bye!")