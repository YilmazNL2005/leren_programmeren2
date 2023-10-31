aanwezig_gastheer = input("Is er een gastheer aanwezig? ")
aanwezig_gasten = input("Zijn er gasten aanwezig? ")
aanwezig_dranken = input("Is er drank aanwezig? ")
aanwezig_chips = input("Is er chips aanwezig? ")
naam_gastheer = input("Wat is de naam van de gastheer? ")

#gastheer = aanwezig_gastheer == "ja" and naam_gastheer != "oorschot"
#gastheer_fout = naam_gastheer != 
#gasten = aanwezig_gasten == "ja"
#drank = aanwezig_dranken == "ja"
#chips = aanwezig_chips == "ja"


# party_a = gasten and chips and drank
# party_b = gastheer and drank

gasten_ok = aanwezig_gasten == "ja" and aanwezig_chips == "ja" and aanwezig_dranken == "ja" and naam_gastheer != "oorschot" # gasten als ze aanwezig zijn en chips aanwezig
gastheer_slb = naam_gastheer != "oorschot" or aanwezig_chips == "ja" and aanwezig_dranken == "ja" # als het niet oorschot beginnen mits er wel drank en chips aanwezig is
gastheer_yilmaz = naam_gastheer == "yilmaz" # alleen in geval van Yilmaz = altijd feest

if gasten_ok or gastheer_slb or gastheer_yilmaz == True:
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