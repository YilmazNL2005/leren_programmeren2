# Stel: je gaat met 3 vrienden (dus met zijn vieren) een dag naar de speelhal: ‘de Speelhal-dag’
# Dat kost een toegangsticket per persoon van 7,45 euro voor de hele dag. 
# Jullie willen ook met zijn allen voor 45 minuten in de VIP-VR-GameSeat. 
#De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten. Jij trakteert dus betaal je alles.

# Maak een programma speelhal.py voor deze berekening.
PRIJS_TOEGANGSTICKET = 7.45
PRIJS_PER_MIN = 0.074
aantal_tickets = int(input("Hoeveel toegangstickets wil je kopen? "))
tijd_vr = int(input("Hoeveel minuten wil je op de Vr gamebril spelen?"))

berekening_vr = PRIJS_PER_MIN * tijd_vr
berekening_tickets = PRIJS_TOEGANGSTICKET * aantal_tickets

print(f"Jullie zijn met {aantal_tickets} mensen. De prijs voor de tickets is in totaal {berekening_tickets} euro")
print(f"Je mag voor {berekening_vr} euro. {tijd_vr} minuten op de vr gamen.")