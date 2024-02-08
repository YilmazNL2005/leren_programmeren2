import random

snoep_kleuren = ("oranje", "blauw", "groen", "bruin")
aantal = int(input("Hoeveel M&M's moeten er in de zak toegevoegd worden? "))
for x in range(0, aantal):
    y = random.randint(0,3)
    print(snoep_kleuren[y])

