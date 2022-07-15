# newDictionary = {"name": "Raj", "branch": "CSE", "USN": "064"}
# print(newDictionary)
# print(type(newDictionary))
# print(newDictionary["name"])
# newDictionary["name"] = "Ravi"
# print(newDictionary)
# newDictionary["CGPA"] = 8.0
# print(newDictionary)

# newDictionary["USN"] = "065"
# print(newDictionary)


# for a in range(5):
#     print(a)

# i = 1
# while i <= 20:
#     print(i)
#     i += 3

# i = 1
# while i <= 100:
#     if i % 5 == 0:
#         print(i)

#     i += 1

# studentName = []
# usnList = []

# for i in range(3):
#     name = input("name:")
#     studentName.append(name)
#     usn = input("usn:")
#     usnList.append(usn)
# print(studentName)
# print(usnList)

items = []
unitItems = []
priceItems = []
totalPrice = 0
for i in range(5):
    item = input("item name:")
    items.append(item)
    units = input("units:")
    unitItems.append(units)
    price = input("Price:")
    priceItems.append(price)
    totalPrice += int(units) * int(price)

print("items Name ******* units ******* price")
for i in range(5):
    print(items[i], "******", unitItems[i], "******", priceItems[i])

print("the total Price is ", totalPrice)

print(items)
print(unitItems)
print(priceItems)
