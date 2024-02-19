from fruitmand import fruitmand
fruitmand.append({
    'name' : 'watermeloen',
    'weight' : 2000,
    'color' : 'groen',
    'round' : True
})
print(fruitmand[7]["name"])
totaal_gewicht = 0
for x in range(len(fruitmand)):
    totaal_gewicht += fruitmand[x]["weight"]
print(totaal_gewicht)