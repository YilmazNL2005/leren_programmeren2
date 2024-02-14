boodschappenlijst = {}
choose_product = True
while choose_product:
    ask_item = input("Wat wil je op het boodschappenlijstje zetten? ").lower()
    ask_count = int(input(f"Hoeveel {ask_item} wil je? "))
    if ask_item not in boodschappenlijst:
        boodschappenlijst[ask_item] = ask_count
    else:
        boodschappenlijst[ask_item] += ask_count 
    print(boodschappenlijst)
    continue_stop = input("Wil je doorgaan met items toevoegen of (type stop) stoppen? \n ")
    if continue_stop == "stop":
        choose_product = False

print("---  Boodschappenlijst  ---", "\n")

for key, value in boodschappenlijst.items():
    print(key, " : ", value, "X")
print("")
print("-------------------------")