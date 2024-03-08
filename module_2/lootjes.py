# Onderstaande Comments is code wat in eerste instantie gebruikt zou worden maar door een onbekende fout gekopieerd en onderaan verbeterd.



# import random

# aantal_deelnemers = 0
# lijst_deelnemers_a = []
# nieuwe_deelnemer = ""
# meer_deelnemers = ""

# while True:
#     if aantal_deelnemers >= 3:
#         meer_deelnemers = input(f"Er zijn nu {aantal_deelnemers} deelnemers. Wil je er nog één toevoegen? (Zo niet, typ nee) ").lower()
#         if meer_deelnemers == "nee":
#             break
#     nieuwe_deelnemer = input("Vul een naam in ").lower()
#     if nieuwe_deelnemer not in lijst_deelnemers_a:
#         aantal_deelnemers += 1
#         lijst_deelnemers_a.append(nieuwe_deelnemer)
#         print(lijst_deelnemers_a, "\n")

# lootjes = {}
# reset_lijst_deelnemers = lijst_deelnemers_a
# lijst_deelnemers_b = lijst_deelnemers_a

# while True:
#     getrokken_a = random.choice(lijst_deelnemers_a)
#     getrokken_b = random.choice(lijst_deelnemers_b)
#     if len(lootjes) == aantal_deelnemers:
#         break
#     elif getrokken_a != getrokken_b and getrokken_a not in lootjes and getrokken_b not in lootjes:
#         lootjes[getrokken_a] = getrokken_b
#         lijst_deelnemers_a.remove(getrokken_a)
#         lijst_deelnemers_b.remove(getrokken_b)
#         print(lootjes)
#     else:
#         lijst_deelnemers_a = reset_lijst_deelnemers
#         lijst_deelnemers_b = reset_lijst_deelnemers
#         lootjes.clear()
# print(lootjes)

import random

aantal_deelnemers = 0
lijst_deelnemers_a = []

nieuwe_deelnemer = ""
meer_deelnemers = ""

while True:
    if aantal_deelnemers >= 3:
        meer_deelnemers = input(f"Er zijn nu {aantal_deelnemers} deelnemers. Wil je er nog één toevoegen? (Zo niet, typ nee) ").lower()
        if meer_deelnemers == "nee":
            break
    nieuwe_deelnemer = input("Vul een naam in ").lower()
    if nieuwe_deelnemer not in lijst_deelnemers_a:
        aantal_deelnemers += 1
        lijst_deelnemers_a.append(nieuwe_deelnemer)
        print(lijst_deelnemers_a, "\n")

lootjes = {}
reset_lijst_deelnemers = lijst_deelnemers_a.copy()
lijst_deelnemers_b = lijst_deelnemers_a.copy()

while True:
    if len(lootjes) == aantal_deelnemers:
        break
    getrokken_a = random.choice(lijst_deelnemers_a)
    getrokken_b = random.choice(lijst_deelnemers_b)
    if getrokken_a != getrokken_b:
        lootjes[getrokken_a] = getrokken_b
        lijst_deelnemers_a.remove(getrokken_a)
        lijst_deelnemers_b.remove(getrokken_b)
        # print(lootjes)
    else:
        lijst_deelnemers_a = reset_lijst_deelnemers.copy()
        lijst_deelnemers_b = reset_lijst_deelnemers.copy()
        lootjes.clear()
        # print("opnieuw")
print(lootjes)

inzien_lootje = input("Om te kunnen zien wie je hebt getrokken, moet je je naam invullen. ")
print("Je hebt:", lootjes[inzien_lootje], "getrokken" )
