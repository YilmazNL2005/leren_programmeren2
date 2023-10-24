a = int(input("Vul een getal in. "))
b = int(input("Vul nog een getal in. "))
max = 0
if a > b:
    max = a
    min = b
elif a < b:
    max = b
    min = a
else:
    max = a
    min = a
    print("a en b zijn even groot")

print(f"Het minimum is: {min}")
print(f"Het maximum is: {max}")