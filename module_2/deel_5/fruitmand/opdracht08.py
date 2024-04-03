from fruitmand_2 import fruitmand
fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 2000,
    'color' : 'groen',
    'round' : True
})

for y in range(len(fruitmand)):
    if fruitmand[y]["name"] == 'watermeloen':
        print(fruitmand[y]["name"])

totaal_gewicht = 0
for fruit in fruitmand:
    totaal_gewicht += fruit["weight"]
print(f"{totaal_gewicht / 1000} kg")
