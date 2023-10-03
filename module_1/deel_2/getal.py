# Maak een programma dat 2 gehele getallen opvraagt aan de gebruiker. 
# Stel die getallen zijn toegekend aan de variabelen a en b
# Bepaal (met een if-statement) of a groter is dan b
# Zo ja:
# Ken de waarde van a toe aan een variabele Max
# Laat het programma printen: ‘a is het grootste getal: ’ gevolgd door de waarde van max
# Doe een commit met de titel “input en if-statement”

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