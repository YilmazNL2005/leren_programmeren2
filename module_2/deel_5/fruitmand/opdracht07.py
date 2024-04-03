from fruitmand_2 import fruitmand
# for x in range(len(fruitmand)):
#     fruit = fruitmand[x]["round"]
#     if fruit == False:
#         print(fruitmand[x]["name"])
for fruit in fruitmand:
    if fruit["round"]:
        print(fruit["name"])