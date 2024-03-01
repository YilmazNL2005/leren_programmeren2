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
verschil = abs(aantal_rond - aantal_niet_rond)

if aantal_rond > aantal_niet_rond:
    print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleur}")
elif aantal_niet_rond > aantal_rond:
    print(f"Er zijn {verschil} meer niet ronde vruchten dan ronde vruchten in de kleur {gekozen_kleur}")
else:
    print(f"Er zijn {aantal_rond} ronde vruchten en {aantal_niet_rond} niet ronde vruchten.")