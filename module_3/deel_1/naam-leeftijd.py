def naam_leeftijd(name, age, info):
    info["naam"] = name
    info["leeftijd"] = age
    return info

naam = input("Wat is je naam? ")
leeftijd = int(input("Wat is je leeftijd in jaren? "))

informatie =    {"naam" : None,
                "leeftijd" : None}

teruggave = naam_leeftijd(naam, leeftijd, informatie)
print(teruggave)

print(f"{teruggave['naam']} is {teruggave['leeftijd']} jaar oud.")