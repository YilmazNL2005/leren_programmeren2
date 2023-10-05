PRIJS_TOEGANGSTICKET = int(input("Hoeveel kost een Toegangsticket pp in centen? "))
PRIJS_PER_5MIN = int(input("Wat is de prijs per 5 minuten in centen? "))
aantal_tickets = int(input("Hoeveel toegangstickets wil je kopen? "))
tijd_vr = int(input("Hoeveel minuten wil je op de Vr gamebril spelen?"))

berekening_vr = PRIJS_PER_5MIN / 5 * tijd_vr
berekening_tickets = PRIJS_TOEGANGSTICKET * aantal_tickets
totaal = berekening_tickets + berekening_vr
print(f"Jullie zijn met {aantal_tickets} mensen. De prijs voor de tickets is in totaal {berekening_tickets} euro")
print(((f"""Dit geweldige dagje-uit met {aantal_tickets} mensen in de speelhal. 
    Met {tijd_vr} VR kost je maar {berekening_vr / 100:.2f} euro. {tijd_vr} minuten op de vr gamen.
    In totaal betaal je dus {totaal / 100:.2f} euro.
    """)))