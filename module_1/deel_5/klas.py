antwoord = None
lijst_namen = []
while antwoord != "nee":
    antwoord = input("Welke naam wil je toevoegen aan de lijst? ")
    if antwoord != "nee" and antwoord not in lijst_namen:
        lijst_namen.append(antwoord)

lijst_namen.reverse()
for x in range(len(lijst_namen)):
    print(lijst_namen[x])