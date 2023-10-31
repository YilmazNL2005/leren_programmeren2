PRIJS_KLEIN = 3.99
PRIJS_MIDDEL = 6.99
PRIJS_GROOT = 11.99

def get_int(aantal_opgeven):
    while True:
        try:
            return int(input(aantal_opgeven))
        except ValueError:
            print("Dit is geen getal, maar een woord of letter.")
            print("Het opgegeven aantal moet opnieuw worden gegeven. Vul een heel getal in om je bestelling te plaatsen")


aantal_klein = get_int("Hoeveel kleine pizza's wil je? ")
aantal_middel = get_int("Hoeveel middel pizza's wil je? ")
aantal_groot = get_int("Hoeveel groot pizza's wil je? ")

totaal_prijs = PRIJS_KLEIN * aantal_klein + PRIJS_MIDDEL * aantal_middel + PRIJS_GROOT * aantal_groot 

print("_____________________________________________________\n")

print(f" Kleine pizza's  {aantal_klein} stuks.        Prijs    {PRIJS_KLEIN * aantal_klein}  euro.")
print(f" Middel pizza's  {aantal_middel} stuks.        Prijs    {PRIJS_MIDDEL * aantal_middel} euro.")
print(f" Grote  pizza's  {aantal_groot} stuks.        Prijs    {PRIJS_GROOT * aantal_groot} euro. \n")

print(f" Totaal                                   {round(totaal_prijs, 2)} euro. ")

print("_____________________________________________________\n")