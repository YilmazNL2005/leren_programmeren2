print("Je zal nu een aantal vragen krijgen om te kijken of je in aanmerking komt voor een sollicitatiegesprek:")

snor = 0
haar_k = ""
haar_l = 0
ondernemer_t = 0
aantal_medewerkers = 0

rijbewijs = input("Ben je in het bezit van een geldig vrachtwagen rijbewijs? ja/nee ")
hoed = input("Ben je in het bezit van een hoge hoed? ja/nee ")
GEWICHT = float(input("Hoe zwaar ben je in kg? "))
LENGTE = int(input("Hoe lang ben je in centimeter? "))
certificaat = input("Heb je een certificaat voor 'Overleven met gevaarlijk personeel'? ja/nee ")
DIEREN_DRESSUUR = float(input("Hoelang heb je praktijkervaring met dieren-dressuur? Geef het antwoord in jaren. "))
JONGLEREN = float(input("Hoelang heb je ervaring met jongleren? Geef het antwoord in jaren. "))
ACROBATIEK = float(input("Hoelang heb je ervaring met acrobatiek? Geef het antwoord in jaren. "))
diploma = input("Ben je in het bezit van een MBO-4 ondernemen diploma? ja/nee ")
ondernemer = input("Ben je een ondernemer? ")
if ondernemer == "ja":
    TIJD_ONDERNEMER = float(input("Hoelang ben je al ondernemer? Geef het antwoord in jaren. "))
    ondernemer_t = TIJD_ONDERNEMER
    MEDEWERKERS = int(input("Hoeveel medewerkers heb je in loondienst? "))
    aantal_medewerkers = MEDEWERKERS
geslacht = input("Wat is je geslacht? man/vrouw ")
if geslacht == "man":
    SNOR = int(input("Hoe breed is je snor in centimeters? "))
    snor = SNOR
elif geslacht == "vrouw":
    kleur_haar = input("Welk haarkleur heb je en wat voor soort haar heb je? bijvoorbeeld krulhaar, los lang, kort. ")
    haar_k = kleur_haar
    HAARLENGTE = int(input("Hoe lang is je haar in centimeters? "))
    haar_l = HAARLENGTE

rijbewijs_ok = rijbewijs == "ja"
hoed_ok = hoed == "ja"
GEWICHT_OK = GEWICHT >= 90 and GEWICHT <= 120
LENGTE_OK = LENGTE >= 150 and LENGTE <= 220
certificaat_ok = certificaat == "ja"
DIEREN__JONG_ACRO_OK = DIEREN_DRESSUUR >= 4 or JONGLEREN >= 5 or ACROBATIEK >= 3
DIPLOMA_OK = diploma == "ja" #or 
ONDERNEMER_TIJD_MEDEWERKERS_OK = ondernemer_t >= 3 and aantal_medewerkers >= 5
SNOR_OK = snor >= 10 #or 
HAARKLEUR_LENGTE_OK = haar_k == "rood krulhaar" and haar_l >= 20
reden_afwijzing = ["rijbewijs bezit je niet", "je bezit geen hoed", "je hebt niet het juiste gewicht", "je hebt niet de juiste lengte", "je hebt geen certificaat", "je hebt te weinig ervaring met dieren_dressuur, Jongleren of Acrobatiek", "je hebt geen diploma", "je bent geen of niet lang genoeg ondernemer of je hebt te weinig medewerkers in loondienst", "je snor is niet breed genoeg", "je haarkleur/haarlengte is niet juist"]

criteria_voldoening = [rijbewijs_ok, hoed_ok, GEWICHT_OK, LENGTE_OK, certificaat_ok, DIEREN__JONG_ACRO_OK, DIPLOMA_OK, ONDERNEMER_TIJD_MEDEWERKERS_OK, SNOR_OK, HAARKLEUR_LENGTE_OK]
criteria_ontbreekt = []
if rijbewijs_ok and hoed_ok and GEWICHT_OK and LENGTE_OK and certificaat_ok and (DIEREN__JONG_ACRO_OK) and (DIPLOMA_OK or ONDERNEMER_TIJD_MEDEWERKERS_OK) and (SNOR_OK or HAARKLEUR_LENGTE_OK):
    print("Je komt in aanmerking voor een sollicitatiegesprek. Stuur je cv naar ons op. ")
else:
    print("Helaas, je komt niet in aanmerking voor een sollicitatie gesprek. ")
    print("Dit is de reden waarom je niet in aanmerking komt voor een sollicitatie gesprek: \n ")
    for punt in range(len(criteria_voldoening)):
        if criteria_voldoening[punt] != True:
            criteria_ontbreekt.append(reden_afwijzing[punt])
    print(criteria_ontbreekt)

# print("Je zal nu een aantal vragen krijgen om te kijken of je in aanmerking komt voor een sollicitatiegesprek:")
# rijbewijs = input("Ben je in het bezit van een geldig vrachtwagen rijbewijs? ja/nee ")
# hoed = input("Ben je in het bezit van een hoge hoed? ja/nee ")
# GEWICHT = float(input("Hoe zwaar ben je in kg? "))
# LENGTE = int(input("Hoe lang ben je in centimeter? "))
# certificaat = input("Heb je een certificaat voor 'Overleven met gevaarlijk personeel'? ja/nee ")
# DIEREN_DRESSUUR = float(input("Hoelang heb je praktijkervaring met dieren-dressuur? Geef het antwoord in jaren. "))
# JONGLEREN = float(input("Hoelang heb je ervaring met jongleren? Geef het antwoord in jaren. "))
# ACROBATIEK = float(input("Hoelang heb je ervaring met acrobatiek? Geef het antwoord in jaren. "))
# diploma = input("Ben je in het bezit van een MBO-4 ondernemen diploma? ja/nee ")
# ondernemer = input("Ben je een ondernemer? ")
# if ondernemer == "ja":
#     TIJD_ONDERNEMER = float(input("Hoelang ben je al ondernemer? Geef het antwoord in jaren. "))
#     MEDEWERKERS = int(input("Hoeveel medewerkers heb je in loondienst? "))
# geslacht = input("Wat is je geslacht? man/vrouw ")
# if geslacht == "man":
#     snor = int(input("Hoe breed is je snor in centimeters? "))
# elif geslacht == "vrouw":
#     kleur_haar = input("Welk haarkleur heb je en wat voor soort haar heb je? bijvoorbeeld krulhaar, los lang, kort. ")
#     haarlengte = int(input("Hoe lang is je haar in centimeters? "))

# if rijbewijs and hoed == "ja" and GEWICHT >= 90 and GEWICHT <= 120 and LENGTE >= 150 and LENGTE <= 220 and certificaat == "ja" and (DIEREN_DRESSUUR >= 4 or JONGLEREN >= 5 or ACROBATIEK >= 3) and (diploma == "ja" or TIJD_ONDERNEMER >= 3 and MEDEWERKERS >= 5) and (snor >= 10 or kleur_haar == "rood krulhaar" and haarlengte >= 20):
#     print("Je komt in aanmerking voor een sollicitatiegesprek. Stuur je cv naar ons op. ")
# else:
#     print("Helaas, je komt niet in aanmerking voor een sollicitatie gesprek. ")
#     print("Je voldoet niet aan alle vereisten dat een medewerker binnen ons bedrijf moet hebben. ")