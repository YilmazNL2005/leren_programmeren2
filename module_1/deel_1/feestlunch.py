croissant = int(input("Hoeveel croissantjes wil je hebben? "))
stokbrood = int(input("Hoeveel stokbroden wil je hebben? "))
kortingsbon = int(input("Hoeveel kortingsbonnen heb je? "))
korting = 50 * kortingsbon
prijs_croissant = 39 * croissant
prijs_stookbrood = 278 * stokbrood
totaalprijs = prijs_croissant + prijs_stookbrood - korting

print(f"Je hebt {croissant} croissantjes. Prijs is {prijs_croissant / 100} euro.")
print(f"Je hebt {stokbrood} stokbroden. Prijs is {prijs_stookbrood / 100} euro.")
print(f"Je hebt {kortingsbon} aantal. Je korting is {korting / 100} euro.")
print(f"In totaal voor {croissant} croissantjes en {stokbrood} stokbroden met {kortingsbon} kortingsbonnen, betaal je in totaal {totaalprijs / 100} euro.")