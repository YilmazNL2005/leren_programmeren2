from fruitmand import fruitmand
for x in range(len(fruitmand)):
    fruit = fruitmand[x]["name"]
    if fruit == "appel":
        print(fruitmand[x]["weight"])