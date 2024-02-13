import random

nummer = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "heer", "vrouw", "boer", "aas"]
soorten_kaarten = ["harten", "schoppen", "ruiten", "klaver"]
stapel = ["joker", "joker"]


# Hier wordt de stapel met kaarten gemaakt
for soort in soorten_kaarten: # soort    soorten_kaarten heeft 4 items
    for num in nummer:        # num      nummer heeft 13 items
        kaart = soort + " " + num + " "
        if soort == "schoppen" or soort == "klaver":
            kaart += "zwart"
        else:
            kaart += "rood"
        stapel.append(kaart)

#Hier wordt de stapel kaarten geschud
random.shuffle(stapel)

# Hier worden de kaarten getrokken

hand = []

# for x in range(7):                                  
#     getrokken_kaart = stapel[0]
#     hand.append(getrokken_kaart)
#     stapel.remove(getrokken_kaart)
#     print(f"kaart {x + 1} : {(hand[x])}")
#     print(f"{x} ")
# hand = []
# for z in range(7):
#     hand.append(stapel.pop(0))
#     print(f"kaart {z + 1} : {(hand[z])}")

for y in range(7):
    print(f"kaart {y + 1} {stapel.pop(0)}")

# stapel is de list met alle kaarten
# getal geeft de positie van het item aan en daarvoor wordt dat item toegevoegd
# getrokken_kaart zegt het al
# hand.append is waar de getrokken_kaart aan wordt toegevoegd
# stapel.remove verwijderd de getrokken_kaart van de stapel
# de print zegt de hoeveelste kaart de gebruiker trekt dus kaart en dan eerst 1
#       daarna toont de print de eerste kaart met behulp van hand
#       De x geeft de positie aan van de kaart in hand


print(f"\n" "Deck van", (len(stapel)), "kaarten:" "\n",
        stapel)