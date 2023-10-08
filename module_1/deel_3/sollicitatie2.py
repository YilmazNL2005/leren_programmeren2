print("Je zal nu een aantal vragen krijgen om te kijken of je in aanmerking komt voor een sollicitatiegesprek:")
rijbewijs = input("Ben je in het bezit van een geldig vrachtwagen rijbewijs? ja/nee ")
hoed = input("Ben je in het bezit van een hoge hoed? ja/nee ")
GEWICHT = float(input("Hoe zwaar ben je in kg? "))
LENGTE = int(input("Hoe lang ben je in centimeter? "))
certificaat = input("Heb je een certificaat voor 'Overleven met gevaarlijk personeel'? ja/nee ")
DIEREN_DRESSUUR = float(input("Hoelang heb je praktijkervaring met dieren-dressuur? Geef het antwoord in jaren. "))
JONGLEREN = float(input("Hoelang heb je ervaring met jongleren? Geef het antwoord in jaren. "))
ACROBATIEK = float(input("Hoelang heb je ervaring met acrobatiek? Geef het antwoord in jaren. "))

if rijbewijs and hoed == "ja" and GEWICHT >= 90 and GEWICHT <= 120 and LENGTE >= 150 and LENGTE <= 220 and certificaat == "ja" and (DIEREN_DRESSUUR >= 4 or JONGLEREN >= 5 or ACROBATIEK >= 3):
    print("Je komt in aanmerking voor een sollicitatiegesprek. Stuur je cv naar ons op. ")
else:
    print("Helaas, je komt niet in aanmerking voor een sollicitatie gesprek. ")