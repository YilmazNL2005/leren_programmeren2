def vraag_getal(antwoord):
    aantal = input("Voer het "+antwoord+" getal in: ")
    getal = int(aantal)
    return getal

def deel_getallen(a, b):
    antwoord = a / b
    return antwoord

getal_1 = vraag_getal("eerste")
getal_2 = vraag_getal("tweede")

if getal_2 == 0:
    print("Kan niet delen door 0")
else:
    resultaat = deel_getallen(getal_1, getal_2)
    print("{} gedeeld door {} is gelijk aan {}".format(getal_1, getal_2, resultaat))