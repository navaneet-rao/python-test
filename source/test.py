a = int(input("Enter the first number = "))
b = int(input("Enter the second number = "))
c = int(input("Enter the third number = "))

if a > b and a > c:
    print(a, " number is larger")
elif b > a and b > c:
    print(b, "number is larger")
elif c > b and c > a:
    print(c, "number is larger")
else:
    print("INVALID number")
