from fruitmand_2 import fruitmand

for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit)
print("")
print(fruitmand)

lijst_kleuren = []
for fruit in fruitmand:
    if fruit['color'] not in lijst_kleuren:
        lijst_kleuren.append(fruit["color"])
print(lijst_kleuren)