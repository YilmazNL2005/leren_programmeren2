import random
zak_M_M = []
snoep_kleuren = ("oranje", "blauw", "groen", "bruin")
aantal = int(input("Hoeveel M&M's moeten er in de zak toegevoegd worden? "))
aantal_blauw = 0

for x in range(aantal):
    kleur = random.choice(snoep_kleuren)
    if kleur == "blauw":
        aantal_blauw += 1
        if aantal_blauw > 5:
            kleur = "groen"
    zak_M_M.append(kleur)


print(zak_M_M)