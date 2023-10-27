aanwezig_gastheer = input("Is er een gastheer aanwezig? ")
aanwezig_gasten = input("Zijn er gasten aanwezig? ")
aanwezig_dranken = input("Is er drank aanwezig? ")
aanwezig_chips = input("Is er chips aanwezig? ")
naam_gastheer = input("Wat is de naam van de gastheer? ")

gastheer = aanwezig_gastheer == "ja" and naam_gastheer != "oorschot"
#gastheer_fout = naam_gastheer != 
gasten = aanwezig_gasten == "ja"
drank = aanwezig_dranken == "ja"
chips = aanwezig_chips == "ja"


party_a = gasten and chips and drank
party_b = gastheer and drank


if party_a or party_b or naam_gastheer == "yilmaz" :
    print('Start the Party')
else:
    print('No Party')

# Maak van de gastheer variable in plaats van een boolean een input. 
# Hierin vraag je de gebruiker de volgende vraag: “Wie is de gastheer?”.

# Breid nu je programma uit (dus niet een nieuw bestand) dat het ook nog werkt met de volgende stellingen:

# Als de naam van de gastheer het zelfde is als jouw naam, dan is er hoe dan ook een feest.
# Als de naam van de gastheer het zelfde is als jouw SLB-er dan is er hoe dan ook geen feest.
# Let op: Zorg er voor dat de punten uit de vorige opdracht ook werken, 
# als je geen naam invult bij de vraag in je terminal dan betekend dit dat er geen gastheer is. 
# Je mag geen nieuwe if’s aanmaken!