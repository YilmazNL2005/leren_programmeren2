gastheer = True
gasten = True
drank = True
chips = True

aanwezig_gastheer = input("Is er een gastheer op de party? ")
if aanwezig_gastheer == "nee":
    gastheer = False
aanwezig_gasten = input("Zijn er gasten op de party? ")
if aanwezig_gasten == "nee":
    gasten = False
aanwezig_drank = input("Is er drank op de party? ")
if aanwezig_drank == "nee":
    drank = False
aanwezig_chips = input("Is er chips op de party? ")
if aanwezig_chips == "nee":
    chips = False

if gastheer and chips and drank == True or gasten and chips and drank == True or gastheer and drank == True :
    print('Start the Party')
else:
    print('No Party')