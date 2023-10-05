croissant = int(input("Hoeveel croissantjes wil je hebben? "))
stokbrood = int(input("Hoeveel stokbroden wil je hebben? "))
kortingsbon = int(input("Hoeveel kortingsbonnen heb je? "))

korting = int(input("Wat is de kortingsprijs per kortingsbon? In centen "))
croissant_prijs = int(input("Wat is de prijs van een croissant per stuk? In centen "))
stokbrood_prijs = int(input("Wat is de prijs van een stokbrood per stuk? In centen "))

totale_korting = korting * kortingsbon
totaalprijs_croissant = croissant_prijs * croissant
totaalprijs_stookbrood = stokbrood_prijs * stokbrood
totaalprijs = totaalprijs_croissant + totaalprijs_stookbrood - totale_korting

print(f"Je hebt {croissant} croissantjes. Prijs is {totaalprijs_croissant / 100} euro.")
print(f"Je hebt {stokbrood} stokbroden. Prijs is {totaalprijs_stookbrood / 100} euro.")
print(f"Je hebt {kortingsbon} aantal. Je korting is {totale_korting / 100} euro.")
print(f"In totaal voor {croissant} croissantjes en {stokbrood} stokbroden met {kortingsbon} kortingsbonnen, betaal je in totaal {totaalprijs / 100} euro.")