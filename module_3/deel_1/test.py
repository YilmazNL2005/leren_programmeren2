# lijstje = ["appel", "banaan", "peer", "watermeloen", "bosbes", "citroen", "druif"]
# print(lijstje)
# onbekende_werking = lijstje[1:6:2]
# print(onbekende_werking)

zin = "Dit is een voorbeeldzin"
woorden = zin.split()
aantal = 0
for woord in woorden:
    aantal += len(woord)
    print(woord)
print(aantal)
print(len(woorden))
halveren = aantal / len(woorden)
print(halveren)

# def functie(woord_of_zin:str) -> float:
#     wobbelwobbel = woord_of_zin.split() # De split zorgt ervoor dat de string wordt opgesplitst in een lijst. Dus elk woord is een item met een eigen index.
#     blork = 0
#     for snorkelwagen in wobbelwobbel: # For loop
#         blork += len(snorkelwagen)

#     bizarro_matrix = blork / len(wobbelwobbel)
#     return print(bizarro_matrix)