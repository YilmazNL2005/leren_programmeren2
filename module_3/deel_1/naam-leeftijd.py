def vraag_naam(vraag_n):
    return vraag_n
def vraag_leeftijd(vraag_l):
    return vraag_l

naam = input("Wat is je naam? ")
leeftijd = int(input("Wat is je leeftijd in jaren? "))

informatie =    {"naam" : None,
                "leeftijd" : None}

naam_terug = vraag_naam(naam)
leeftijd_terug = vraag_leeftijd(leeftijd)
# print(naam)
# print(leeftijd_terug)
informatie["naam"] = naam_terug
informatie["leeftijd"] = leeftijd_terug
# print(informatie) 
print(f"{informatie['naam']} is {informatie['leeftijd']} jaar oud.")