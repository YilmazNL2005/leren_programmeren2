hoeveelheid_lijstjes = int(input("Hoeveel lijstjes? "))

lijstje = []

for a in range(hoeveelheid_lijstjes):
    hoeveelheid_items = int(input(f"Hoeveel items in lijst {a+1}? "))
    enkele_lijst = []
    for b in range(1, hoeveelheid_items + 1):
        enkele_lijst.append(b * (a + 1))
    lijstje.append(enkele_lijst)

print(lijstje)