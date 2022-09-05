
list1 = []
matchpoint = [9,4,3,8,10,6]
print(matchpoint[0])
print(matchpoint[3])
print(matchpoint[5])
print("total number:", matchpoint[0] + matchpoint[3] + matchpoint[5])


numberlist = []
numberlist.append(9)
numberlist.append(3)
numberlist.append(6)

shoppinglist = ['apple', 'banana', 'fish', 'meat', 'chicken']
print(shoppinglist)
shoppinglist.insert(3, "4 eggs")
print(shoppinglist)
shoppinglist.pop(2)
print(shoppinglist)
shoppinglist.remove('banana')
print(shoppinglist)

name = []
name = input("Enter your name:")
index = 0
while name != "" and index < len(name):
    print(name[index])
    index += 1

name = input("Enter your name:")
for character in name:
    print(character)

for number in range(1,10,2):
    print(number)

for number in range(4):
    print("I am so cool!"):

number = list(range(1,5))
print(number)

num = int(input("input a number, 0 or negative to exit:"))
while num > 0:
    result = 1
    for i in range(1,num+1):
         result = result * i
    print(result)
    num = int(input("input a number, 0 or negative to exit:"))


