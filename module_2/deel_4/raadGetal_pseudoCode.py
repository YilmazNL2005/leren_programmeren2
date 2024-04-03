# Start programma

# De gebruiker zal de uitleg van het spel te zien krijgen.

# maxRondes wordt 3
# aantalKansen wordt 10
# huidigeRonde wordt 1
# aantalPunten wordt 0
# Geheimgetal wordt Een getal dat willekeurig zal worden gegenereerd tussen 1 en 1000.

# Zolang aantalKansen groter dan 0 is EN huidigeRonde kleiner is dan maxRondes:
#     Raadgetal wordt input(gebruiker moet een getal tussen 1 - 1000 geven)
#     verschil wordt Geheimgetal min Raadgetal
#     verschil wordt absoluut getal. 
#     Als: Raadgetal hetzelfde is als Geheimgetal:
#         Geheimgetal wordt Nieuw getal tussen 1 - 1000
#         "goed gedaan"
#         huidigeRonde wordt huidigeRonde plus 1
#         aantalPunten wordt aantalPunten plus 1
#         aantalKansen wordt 10
#     Anders:
#          Als: verschil groter is dan 50:
#              "koud"  
#          Anders dan: verschil groter is of gelijk aan 25 EN kleiner of gelijk aan 50:
#             "warm"
#          Anders:
#             "erg warm"
#         Gebruiker ziet de uitkomst ("warm"/"erg warm"/"koud")
#         Als: Geheimgetal; kleiner is dan Raadgetal:
#             "lager"
#         Anders:
#             "hoger"
#         de Gebruiker ziet nu de uitkomst("lager"/"hoger")
#         aantalKansen wordt aantalKansen min 1

# Bij het verliezen of winnen van het spel:

#     Winnen is wanneer alle rondes behaald zijn
#     De gebruiker krijgt zijn score, resterende kansen en behaalde rondes te zien.

#     Verliezen is wanneer aantalkansen op 0 staat
#     De gebruiker krijgt zijn score en behaalde rondes te zien.
