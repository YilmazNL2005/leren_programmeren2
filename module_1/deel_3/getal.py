a = int(input("Vul een getal in. "))
b = int(input("Vul nog een getal in. "))
max = 0
if a > b:
    max = a
    min = b
    print(f"Het minimum is: {min}")
    print(f"Het maximum is: {max}")
elif a < b:
    max = b
    min = a
    print(f"Het minimum is: {min}")
    print(f"Het maximum is: {max}")
else:
    print("a en b zijn even groot")