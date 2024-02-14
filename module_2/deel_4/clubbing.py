PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

# Bouw hieronder de flowchart na

kleur_bandje = "geen bandje"
stempel = "geen stempel"

age = int(input("Hoe oud ben je in hele jaren? "))
if age < 18:
    print("Sorry je mag niet naar binnen.")
    when_access = 18
    print(f"Probeer het in {when_access - age} jaar nog eens. ")
    exit()
else:
    name = input("Wat is je naam? ")
    if name in VIP_LIST:
        if age >= 21:
            kleur_bandje = "blauw"
            print(f"Je krijgt van mij een {kleur_bandje} bandje")
        else:
            kleur_bandje = "rood"
    else:
        if age >= 21:
            stempel = "stempel"
            print(f"Je krijgt van mij een {kleur_bandje}")
    drinks = input("Wat wil je drinken? ").lower()
    if drinks == "cola":
        if kleur_bandje == "geen bandje":
            print(f"Alsjeblieft je {drinks}, dat is dan €{PRIJS_COLA}")
        else:
            print("Alstublieft, complimenten van het huis.")
    if drinks == "bier":
        if kleur_bandje != "geen bandje" or stempel != "geen stempel":
            if kleur_bandje != "geen bandje":
                print("Alstublieft, complimenten van het huis.")
            else:
                print(f"Alsjeblieft je {drinks}, dat is dan €{PRIJS_BIER}")
        else:
            print("Sorry je mag geen alcohol bestellen onder de 21.")
            when_access = 21
            print(f"Probeer het in {when_access - age} jaar nog eens. ")
            exit()
    if drinks == "champagne":
        if kleur_bandje == "geen bandje":
            print("Sorry alleen vips mogen champagne bestellen.")
            exit()
        elif kleur_bandje == "blauw":
            print(f"Alsjeblieft je {drinks}, dat is dan €{PRIJS_CHAMPAGNE}")
        else:
            print("Sorry je mag geen alcohol bestellen onder de 21.")
            when_access = 21
            print(f"Probeer het in {when_access - age} jaar nog eens. ")
            exit()
    else:
        print("Sorry geen idee wat je bedoeld, hier een glaasje water.")