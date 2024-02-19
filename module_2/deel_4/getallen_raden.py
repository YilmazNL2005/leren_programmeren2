import random

MAX_RONDES = 3
aantal_kansen = 10
huidige_ronde = 1
aantal_punten = 0
high_low = ""
raad = 0
how_close = ""



while True:
    start = input("Wil je beginnen? typ (start)").lower()
    if start == "start":
        break

print(f"Welkom bij Raad Het Getal \n Je zult max {MAX_RONDES} spelen. \n Bij elke ronde krijg je een getal tussen de 1 en de 1000. \n Je krijgt in totaal {aantal_kansen} kansen om een getal goed te raden. \n Elke keer als je een getal goed raad, krijg je een punt. \n Het programma zal aangeven hoe dichtbij je in de buurt bent van het getal en of je hoger of lager moet raden. \n Succes!!! ")


teRaden_getal = random.randint(1, 1000)
verschil = teRaden_getal - raad

while aantal_kansen > 0 and huidige_ronde <= MAX_RONDES:
    if teRaden_getal == raad:
        teRaden_getal = random.randint(1, 1000)
    print(teRaden_getal)
    print(f"Dit is ronde: {huidige_ronde} \n Je hebt {aantal_punten} punten \n Je hebt {aantal_kansen} kansen")
    raad = int(input("Noem een getal tussen de 1 en de 1000. \n "))
    verschil = teRaden_getal - raad
    if teRaden_getal == raad:
        print("Goed gedaan je hebt het getal geraden.")
        huidige_ronde += 1
        aantal_punten += 1
    else:
        print(f"Helaas {raad} is niet het juiste getal.")
        aantal_kansen -= 1
        if verschil >= 25 and verschil <= 50:
            how_close = "warm"
        elif verschil > 0 and verschil < 25:
            how_close = "erg warm"
        else:
            how_close = "koud"
        print(f"Je bent {how_close}")
        if teRaden_getal < raad:
            high_low = "lager"
        else:
            high_low = "hoger"
        print(f"Het getal is {high_low} dan {raad} \n")


print(f"Je hebt het gehaald tot ronde: {huidige_ronde - 1}")
print(f"Je hebt: {aantal_punten} punten")
print(f"Je aantal kansen staat op: {aantal_kansen}")
if huidige_ronde < MAX_RONDES:
    print(f"Wie weet haal je het de volgende keer wel tot ronde {MAX_RONDES}")
else:
    print(f"Gefeliciteerd!!! Je hebt alle {MAX_RONDES} rondes weten te behalen")