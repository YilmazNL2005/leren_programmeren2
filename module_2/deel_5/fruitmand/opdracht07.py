from fruitmand import fruitmand
for x in range(len(fruitmand)):
    fruit = fruitmand[x]["round"]
    if fruit == False:
        print(fruitmand[x]["name"])