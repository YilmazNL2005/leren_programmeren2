import random

snoep_kleuren = ["rood", "blauw", "groen", "geel", "bruin"]
hoeveelheid_snoepjes = int(input("Hoeveel snoepjes moeten er toegevoegd worden aan de zak? "))

zak_M_M = {
    # "rood" : 0,
    # "blauw" : 0,
    # "groen" : 0,
    # "geel" : 0,
    # "bruin" : 0
}

for x in range(hoeveelheid_snoepjes):
    gekozen_kleur = random.choice(snoep_kleuren)
    if gekozen_kleur not in zak_M_M:
        zak_M_M[gekozen_kleur] = 1
    else:
        zak_M_M[gekozen_kleur] += 1
    print(zak_M_M)