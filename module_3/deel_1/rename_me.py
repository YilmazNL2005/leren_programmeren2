def is_even(getal:int) -> bool:
    return print(getal % 2 == 0) # Deze functie geeft aan de hand van een True/False value aan of het getal even is of oneven.

def string_changer(woord_zin:str) -> str:
    string_lijst = woord_zin.split() # De split zorgt ervoor dat de string wordt opgesplitst in een lijst. Dus elk woord is een item met een eigen index.
    lijst_omkeren = string_lijst[::-1] # Lijst wordt omgekeerd
    omgekeerde_string = ' '.join(lijst_omkeren) # Na elk item in een list wordt er met een join in dit geval steeds " " geplaatst.
    return print(omgekeerde_string) # Resultaat wordt getoond.

def string_lengte(gegeven_woord:str) -> int: # Deze functie geeft aan hoeveel unieke letters in een string zitten.
    dubbele_letter_vw = set(gegeven_woord) # Set zorgt ervoor dat elke letter max 1 keer voorkomt. De dubbele verwijderd hij.
    aantal_soorten_letters = len(dubbele_letter_vw) # Checkt hoeveel letters nu in de string zitten.
    return print(aantal_soorten_letters) # Aantal letters wordt getoond.

def gemiddelde_letter(woord_of_zin:str) -> float:
    lijst_woorden = woord_of_zin.split() # De split zorgt ervoor dat de string wordt opgesplitst in een lijst. Dus elk woord is een item met een eigen index.
    totaal_letters = 0
    for woord in lijst_woorden: # For loop loopt door de lijst heen.
        totaal_letters += len(woord) # Telt het aantal letters van het item uit de lijst en voegt dat aantal bij het totaal. 

    letters_per_woord = totaal_letters / len(lijst_woorden) # Hier wordt het gemiddelde aantal letters dat per woord wordt gebruikt berekend.
    return print(letters_per_woord) # Deze return laat zien hoeveel letters ieder woord gemiddeld krijgt.

def tafel_van(tafel:int, tot_max:int=10) -> None:
    for aantal_keer in range(1, tot_max+1): # For loop die zorgt dat het aantal keer dat de tafel van ... tot 10 wordt gedaan. 
        berekening_tafel = aantal_keer * tafel # Dit de berekening per aantal tafel. 
        print(f'{aantal_keer} x {tafel} = {berekening_tafel}') # De print toont de berekeningen aan de gebruiker. Door de for loop van regel 25 zal dit in dit geval 10 keer uitgevoerd worden.

is_even(2)
string_changer("Hallo ik ben Yilmaz")
string_lengte("Hallo wereld")
gemiddelde_letter("Dit is een voorbeeldzin")
tafel_van(50)