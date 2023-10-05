# Maak op de plek van ??? in de if één if statement waarbij alle onderstaande stellingen kloppen.

# Alleen chips is geen feest.                                                                       check
# Een feest met chips, maar zonder drank kan niet beginnen.                                         check
# Een feest met gasten kan niet beginnen als er geen chips en geen drank is.                        check
# Een feest moet minimaal gasten of een gastheer hebben.                                            check
# Een gastheer kan een feest geven zonder chips en gasten, maar niet zonder drank.                  check
# Het feest kan alleen beginnen als de gastheer er is, tenzij er gasten, chips en drank zijn.       check

# Let op:  Zorg er voor dat je het goed test. 
# Dit kun je doen door de variabelen op True en/of False te zetten, 
# dit doe je door bijvoorbeeld als je punt 1 wilt testen door gastheer, gasten en drank de waarde False 
# te geven en chips de waarde True, dan het programma “No Party” aan moeten geven.

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