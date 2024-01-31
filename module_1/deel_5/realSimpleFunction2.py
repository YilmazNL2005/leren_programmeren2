import math 
from test_lib import test, report

# bedrag = float(input("Wat is het bedrag? "))
# print(bedrag)

def afgeronding_bedrag(bedrag):
    berekening = round(bedrag * 100 / STUIVER) * STUIVER / 100
    return berekening

bedrag = 2.24
STUIVER = 5
inhoud_parameters = afgeronding_bedrag(bedrag)
print(inhoud_parameters)