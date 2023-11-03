def convertToEuroText (amount):
    return "€{:.2f}".format(float(amount)).replace(".", ",")

SMALL_PRICE = 1.25
MEDIUM_PRICE = 2.10
#Varibelen moet je niet hergebruiken.
amount = float(input('Hoeveel ijsjes van {} wil je bestellen? '.format(convertToEuroText(SMALL_PRICE))))
amount_a = float(input('En hoeveel ijsjes van {} wil je bestellen? '.format(convertToEuroText(MEDIUM_PRICE))))
totalPrice = amount * SMALL_PRICE + amount_a * MEDIUM_PRICE

print('Dat is dan {} totaal'.format(convertToEuroText(totalPrice)))