begingetal = 50
nieuw_getal = 50
print(nieuw_getal)

som = f"50"

while nieuw_getal < 1000:
    begingetal += 1
    nieuw_getal += begingetal
    som += f"+{begingetal}"
    print(f"{som} = {nieuw_getal}")