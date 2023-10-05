gastheer = True
gasten = True
drank = True
chips = True

aanwezig_gastheer = input("Is er een gastheer op de party? ")
if aanwezig_gastheer == "nee":
    gastheer = False
elif aanwezig_gastheer == "ja":
    naam_gastheer = input("Hoe heet de gastheer? ")
    if naam_gastheer == "oorschot" or naam_gastheer == "":
        gastheer = False
        gasten = False
aanwezig_gasten = input("Zijn er gasten op de party? ")
if aanwezig_gasten == "nee":
    gasten = False
elif aanwezig_gasten == "ja":
    aantal_gasten = int(input("Hoeveel gasten zijn er op de party? "))
    if aantal_gasten == 0:
        aanwezig_gasten = False
aanwezig_drank = input("Is er drank op de party? ")
if aanwezig_drank == "nee":
    drank = False
aanwezig_chips = input("Is er chips op de party? ")
if aanwezig_chips == "nee":
    chips = False

if gastheer and chips and drank == True or gasten and chips and drank == True and aantal_gasten >= 4 and aantal_gasten <= 20 or gastheer and drank == True or naam_gastheer == "yilmaz":
    print('Start the Party')
else:
    print('No Party')

# In het kort wanneer een feest kan beginnen

# - als er een gastheer, chips en drank aanwezig is.
# - als er minimaal 4 en maximaal 20 gasten, chips en drank aanwezig is.
# - als er een gastheer en drank aanwezig is.
# - als de naam van de gastheer yilmaz is. 