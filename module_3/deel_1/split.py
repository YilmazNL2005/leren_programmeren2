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
    return





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