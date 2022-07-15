a = float(input("Enter the value of all the 1th subject "))
b = float(input("Enter the value of all the 2nd subject "))
c = float(input("Enter the value of all the 3nd subject "))
d = float(input("Enter the value of all the 4th subject "))
e = float(input("Enter the value of all the 5th subject "))

percent = ((a + b + c + c + d + e) / 500) * 100

print("ur percent is ", percent)
if 100 > percent > 90:
    print("O grade")
elif 90 > percent > 80:
    print("A grade")
elif 80 > percent > 70:
    print("B grade")
elif 70 > percent > 60:
    print("C grade")
elif 60 > percent > 50:
    print("D grade")
elif 50 > percent > 40:
    print("E grade")
elif 40 > percent > 30:
    print("Fail")
else:
    print("invalid")
