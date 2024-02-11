begingetal = 50
getal = 50
print(getal)

som = f"{begingetal} "
begingetal += 1

while getal < 1000:
    getal += begingetal + 1
    som += f" + {begingetal} "
    print(som)
    begingetal += 1
    print(getal)