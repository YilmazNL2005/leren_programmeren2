# Dit moeten de uikomsten worden 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 

def fibonacci(aantal):
    getal1 = 0
    getal2 = 1
    lijst_getallen = [0, 1]
    for x in range(1,aantal+1):
        berekening = getal1 + getal2
        getal1 = getal2
        getal2 = berekening
        lijst_getallen.append(berekening)
    return lijst_getallen

aantaL_getallen = int(input("Hoeveel getallen wil je laten berekenen? "))

reeks = fibonacci(aantaL_getallen)

print(reeks)