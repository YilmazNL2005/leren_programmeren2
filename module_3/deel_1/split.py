from collections import Counter
import math, random

print("Functions onder elkaar: \n")

def getallenlijst_controle(nummers:list):
    if not nummers:
        return {"Er zit niks in de lijst. Doe die erin.":nummers}
    for x in range(len(nummers)):
        if not str(nummers[x]).isnumeric():
            return f"{nummers[x]} is geen nummer."
    return "In deze lijst zitten geen letters of iets dergelijks"

def aantal_nummers(nummers:list):
    return len(nummers)

def totaal_nummers(nummers:list):
    return sum(nummers)

def gemiddeld_nummer(nummers:list):
    return totaal_nummers(nummers) / aantal_nummers(nummers)

def laagste_nummer(nummers:list):
    return min(nummers)

def hoogste_nummer(nummers:list): # Waarom moet er :list staan bij de parameter als de functie zonder dat het ook nog steeds werkt?
    return max(nummers)

def kleinste_delen(nummers:list):
    return laagste_nummer(nummers) / nummers[0]

def grootste_delen(nummers:list):
    return hoogste_nummer(nummers) / nummers[1]

def unieke_nummers(nummers:list):
    return set(nummers)

def aantal_unieke_nummers(nummers:list):
    return len(unieke_nummers(nummers))

def verschil_control_nummer(nummers:list):
    return abs(aantal_unieke_nummers(nummers) - nummers[2])

def lijst_sorteerder(nummers:list):
    return sorted(nummers)

def unieke_lijst_sorteerder(nummers:list):
    return sorted(unieke_nummers(nummers))

def hoeveelheid_unieke_nummers(nummers:list):
    telling_elementen = {}
    for nummer in nummers:
        aantalkeer = telling_elementen[nummer]+1 if nummer in telling_elementen else 1
        telling_elementen[nummer] = aantalkeer
    return telling_elementen

def unieke_nummers_delen_a(nummers:list):
    delen_a = []
    for nummer in nummers:
        if nummer % nummers[1] == 0:
            delen_a.append(nummer)
    return sorted(delen_a)

def unieke_nummers_delen_b(nummers:list):
    delen_b = []
    for nummer in nummers:
        if nummer % 8 == 0:
            delen_b.append(nummer)
    return sorted(delen_b)

def nummer_voorkomen(nummers:list):
    return 69 in nummers and 33 in nummers

def position(nummers:list):
    positie = []
    for index, num in enumerate(nummers):
        if num == 2:
            positie.append(index)
    return positie

def afwijking(nummers:list):
    verschil_kwadraat = sum((x - gemiddeld_nummer(nummers)) ** 2 for x in nummers)
    variantie = verschil_kwadraat / aantal_nummers(nummers)
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking

def shuffle_lijst(nummers:list):
    random.shuffle(nummers)
    return nummers

def random_nummer(nummers:list):
    return nummers[random.randint(0,aantal_nummers(nummers)-1)]

def verschil_control_nummer_b(nummers:list):
    return abs(random_nummer(nummers) - 8)


lijstje_nummers = [1, 10, 33, 9, 81, 69]
print(getallenlijst_controle(lijstje_nummers))
print(aantal_nummers(lijstje_nummers))
print(totaal_nummers(lijstje_nummers))
print(gemiddeld_nummer(lijstje_nummers))
print(laagste_nummer(lijstje_nummers))
print(hoogste_nummer(lijstje_nummers))
print(kleinste_delen(lijstje_nummers))
print(grootste_delen(lijstje_nummers))
print(unieke_nummers(lijstje_nummers))
print(aantal_unieke_nummers(lijstje_nummers))
print(verschil_control_nummer(lijstje_nummers))
print(lijst_sorteerder(lijstje_nummers))
print(unieke_lijst_sorteerder(lijstje_nummers))
print(hoeveelheid_unieke_nummers(lijstje_nummers))
print(unieke_nummers_delen_a(lijstje_nummers))
print(unieke_nummers_delen_b(lijstje_nummers))
print(nummer_voorkomen(lijstje_nummers))
print(position(lijstje_nummers))
print(afwijking(lijstje_nummers))
print(shuffle_lijst(lijstje_nummers))
print(random_nummer(lijstje_nummers))
print(verschil_control_nummer_b(lijstje_nummers))