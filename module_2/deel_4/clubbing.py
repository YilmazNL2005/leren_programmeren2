PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

# Bouw hieronder de flowchart na

ALSJEBLIEFT = "Alstublieft, complimenten van het huis."
SORRY = "Sorry je mag geen alcohol bestellen onder de 21."

def probeer_in_jaar(jaar):
    return f"Probeer het in {jaar} jaar nog eens. "

def bandkleur(kleur):
    return f"Je krijgt van mij een {kleur} bandje"


kleur_bandje = "geen bandje"
stempel = "geen stempel"

age = int(input("Hoe oud ben je in hele jaren? "))
if age < 18:
    print("Sorry je mag niet naar binnen.")
    print(probeer_in_jaar(18 - age))
    exit()
else:
    name = input("Wat is je naam? ")
    if name in VIP_LIST:
        if age >= 21:
            print(bandkleur("blauw"))
        else:
            print(bandkleur("rood"))
    else:
        if age >= 21:
            stempel = "stempel"
            print(f"Je krijgt van mij een {kleur_bandje}")
    drinks = input("Wat wil je drinken? ").lower()
    if drinks == "cola":
        if kleur_bandje == "geen bandje":
            print(f"Alsjeblieft je {drinks}, dat is dan €{PRIJS_COLA}")
        else:
            print(ALSJEBLIEFT)
    elif drinks == "bier":
        if kleur_bandje != "geen bandje" or stempel != "geen stempel":
            if kleur_bandje != "geen bandje":
                print(ALSJEBLIEFT)
            else:
                print(f"Alsjeblieft je {drinks}, dat is dan €{PRIJS_BIER}")
        else:
            print(SORRY)
            print(probeer_in_jaar(21 - age))
            exit()
    elif drinks == "champagne":
        if kleur_bandje == "geen bandje":
            print("Sorry alleen vips mogen champagne bestellen.")
            exit()
        elif kleur_bandje == "blauw":
            print(f"Alsjeblieft je {drinks}, dat is dan €{PRIJS_CHAMPAGNE}")
        else:
            print(SORRY)
            print(probeer_in_jaar(21 - age))
            exit()
    else:
        print("Sorry geen idee wat je bedoeld, hier een glaasje water.")