# De functionaliteiten die in de applicatie moeten zitten zijn:

# de klant kan een keuze maken uit 3 afmetingen pizza's, namelijk: small, medium en large. 
# Voor elke afmeting wordt er gevraagd hoeveel pizza's de klant wil.
# zoek op internet naar passende prijzen voor deze pizza afmetingen 
# en noteer deze prijzen in je applicatie
# Toon op het scherm met goede omschrijving het aantal bestelde pizza's voor elke afmeting 
# en berekenen per afmeting de prijs uit
# Toon op het scherm de totaalprijs van alle pizza's.
# Bovenaan in de Python file noteer je als commenteer het volgende:
# voornaam, achternaam en opdracht: Pizza calculator
# De volgende zaken dienen ook op orde te zijn:

# leesbare layout van de code
# naamgeving is duidelijk en 'self explaining'
# er is passend commentaar toegevoegd in de code
# laat de uitkomst er uit zien als een bonnetje


aantal_klein = 0
aantal_middel = 0
aantal_groot = 0

prijs_klein = 3.99
prijs_middel = 6.99
prijs_groot = 11.99

def get_int(txtInvoer, txtError = None):
    if txtError == None:
        txtError = "Dit is geen getal, maar een woord of letter."
    while True:
        try:
            return int(input(txtInvoer))
        except ValueError:
            print(txtError)

    
aantal_klein = get_int("Hoeveel kleine pizza's wil je? ")
aantal_middel = get_int("Hoeveel middel pizza's wil je? ")
aantal_groot = get_int("Hoeveel groot pizza's wil je? ")

totaal_prijs = prijs_klein * aantal_klein + prijs_middel * aantal_middel + prijs_groot * aantal_groot 

print("_____________________________________________________\n")

print(f" Kleine pizza's  {aantal_klein} stuks.        Prijs    {prijs_klein * aantal_klein}  euro.")
print(f" Middel pizza's  {aantal_middel} stuks.        Prijs    {prijs_middel * aantal_middel} euro.")
print(f" Grote  pizza's  {aantal_groot} stuks.        Prijs    {prijs_groot * aantal_groot} euro. \n")

print(f" Totaal                                   {totaal_prijs} euro. ")

print("_____________________________________________________\n")