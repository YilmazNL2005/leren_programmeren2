aanwezig_gastheer = input("Is er een gastheer aanwezig? ")
aanwezig_gasten = input("Zijn er gasten aanwezig? ")
aanwezig_dranken = input("Is er drank aanwezig? ")
aanwezig_chips = input("Is er chips aanwezig? ")
naam_gastheer = input("Wat is de naam van de gastheer? ")

gastheer = aanwezig_gastheer == "ja" and naam_gastheer != "oorschot"
gasten = aanwezig_gasten == "ja"
drank = aanwezig_dranken == "ja"
chips = aanwezig_chips == "ja"
print(gastheer)
print(gasten)
print(drank)
print(chips)

party_a = gasten  and chips == True and drank == True
party_b = gastheer and drank
print(party_a)
print(party_b)

if party_a == True or party_b == True or naam_gastheer == "yilmaz" or naam_gastheer != "oorschot" or naam_gastheer != "":
    print('Start the Party')
else:
    print('No Party')

