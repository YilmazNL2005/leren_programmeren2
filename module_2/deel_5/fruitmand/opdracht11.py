from fruitmand import fruitmand

gekozen_kleur = input("Noem een kleur. ")
yes_no = "niet"
aantal_rond = 0
aantal_niet_rond = 0
while True:
    for fruit in fruitmand:
        if fruit["color"] == gekozen_kleur:
            yes_no = "wel"
            if fruit["round"] == True:
                aantal_rond += 1
            else:
                aantal_niet_rond += 1
    break
print(f"De kleur {gekozen_kleur} zit {yes_no} in de fruitmand.")
print(f"Er zijn {aantal_rond} ronde fruitsoorten")
print(f"Er zijn {aantal_niet_rond} niet ronde fruitsoorten")

# De opdracht is nog Niet klaar.