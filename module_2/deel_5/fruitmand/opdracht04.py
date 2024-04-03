from fruitmand_2 import fruitmand
import random

aantal_fruit = int(input("Hoeveel fruit wil je? "))
for x in range(aantal_fruit):
    print(fruitmand[random.randint(0,len(fruitmand) - 1)]["name"])