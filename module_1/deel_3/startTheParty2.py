aanwezig_gastheer = input("Is er een gastheer aanwezig? ")
aanwezig_gasten = int(input("Hoeveel gasten zijn eraanwezig? "))
aanwezig_dranken = input("Is er drank aanwezig? ")
aanwezig_chips = input("Is er chips aanwezig? ")
naam_gastheer = input("Wat is de naam van de gastheer? ")

gasten_ok = (aanwezig_gasten >= 4 and aanwezig_gasten < 20 ) and aanwezig_chips == "ja" and aanwezig_dranken == "ja" and naam_gastheer != "oorschot" # gasten als ze aanwezig zijn en chips aanwezig
gastheer_slb = naam_gastheer != "oorschot" and aanwezig_chips == "ja" and aanwezig_dranken == "ja" # als het niet oorschot beginnen mits er wel drank en chips aanwezig is
gastheer_yilmaz = naam_gastheer == "yilmaz" # alleen in geval van Yilmaz = altijd feest

if gasten_ok or gastheer_slb or gastheer_yilmaz == True:
    print('Start the Party')
else:
    print('No Party')