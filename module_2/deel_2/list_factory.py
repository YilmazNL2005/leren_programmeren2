hoeveelheid_lijstjes = int(input("Hoeveel lijstjes wil je? ")) # 3 lijsten

lijstje = []

for a in range(hoeveelheid_lijstjes):
    hoeveelheid_items = int(input(f"Hoeveel items moeten er in lijst {a+1}? ")) # 2 - 5 - 3
    enkele_lijst = []
    for b in range(1, hoeveelheid_items + 1):
        print(b)
        enkele_lijst.append(hoeveelheid_items)
        # enkele_lijst.append(b * (a + 1))
    lijstje.append(enkele_lijst)

print(lijstje)