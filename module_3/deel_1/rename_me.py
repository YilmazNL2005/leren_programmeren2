def is_even(getal:int) -> bool:
    return print(getal % 2 == 0) # Deze functie geeft aan de hand van een True/False value aan of het getal even is of oneven.

def string_changer(woord_zin:str) -> str:
    string_lijst = woord_zin.split() # De split zorgt ervoor dat de string wordt opgesplitst in een lijst. Dus elk woord is een item met een eigen index.
    lijst_omkeren = string_lijst[::-1] # Lijst wordt omgekeerd
    omgekeerde_string = ' '.join(lijst_omkeren) # Na elk item in een list wordt er met een join in dit geval steeds " " geplaatst.
    return print(omgekeerde_string)

def kosmische_koekjesmix(galactische_snoepjes:str) -> int:
    planetair_taartje = set(galactische_snoepjes)
    whatchamacallit = len(planetair_taartje)
    return whatchamacallit

def ruimte_hamsterwiel(planetair_taartje:str) -> float:
    wobbelwobbel = planetair_taartje.split()
    
    blork = 0
    for snorkelwagen in wobbelwobbel:
        blork += len(snorkelwagen)

    bizarro_matrix = blork / len(wobbelwobbel)
    return bizarro_matrix

def spaghetti_spaceship(infinity_pizza:int, parallelle_tosti:int=10) -> None:
    for zwabber_krakeling in range(1, parallelle_tosti+1):
        laser_sandwich = zwabber_krakeling * infinity_pizza
        print(f'{zwabber_krakeling} x {infinity_pizza} = {laser_sandwich}')

is_even(2)
string_changer("Hallo ik ben Yilmaz")