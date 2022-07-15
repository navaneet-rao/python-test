newList = [1, 2, 3, 4, 5]
newList1 = [1.4, 2.5, 3.6, 4.7, 5.6]
newList2 = ["one", "two"]
print(type(newList))
print(newList2)


editable, repetition and ordered


# works for strings too

List = [1, 2, 3, 4, 5]
List1 = []
List2 = ["1", "2", "3", "4", "5"]

List2.insert(2, "10")
print(List[2])
print(List[2:])
print(List[-2:-1])
print(List[2:7])
print(len(List))
List[0:2] = ["hello"]
List1[0:2] = "hello"

print(List)
print(List2)
print(List1)

List2.append(20)
print(List2)

List.pop()
print(List)

List.pop(2)
print(List)

List.clear()
print(List)

del List

one = [1, 2, 3, 4, 5]
two = [6, 7, 8]
three = one + two
print(three)

listOne = ["red", "yellow", "blue", "green", "black"]
print(listOne)
for i in listOne:
    print(i)
    print("Inside the loop")
print("here")

for i in range(5):
    print(i)

for i in range(10):
    print("hello", str(i))

a = int(input("enter the digit: "))
for i in range(1, 11):
    print(a, "*", i, "=", a * i)


a = int(input("enter the range: "))
sum = 0
for i in range(1, a + 1):
    sum = sum + i
print("The sum of N natural numbers is ", sum)


a = []
a = input("enter the elements")
print(a)
for i in a:
    print(i)
