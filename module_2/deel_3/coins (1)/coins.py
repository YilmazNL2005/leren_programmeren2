# name of student: Yilmaz Güney
# number of student: 99069863
# purpose of program: ---
# structure of program: ---

# Print na de while loop ook een overzicht van alle teruggegeven muntstukken: per soort muntstuk hoeveel zijn er teruggeven.


# De comments tonen aan dat je de werking van het programma helemaal hebt begrepen.

coinValues = [500, 200, 100, 50,20,10,5,2,1] # Alle soorten muntgeld dat er bestaat
munt_soorten = {}
toPay = int(float(input('Amount to pay: '))* 100) # Het bedrag dat betaalt moet worden door de klant
paid = int(float(input('Paid amount: ')) * 100) # Met hoeveel geld betaalt de klant word er gevraagd.
change = paid - toPay # Hier word berekent hoeveel wisselgeld de klant terugkrijgt

while change > 0 and len(coinValues) > 0: # Als er geld gewiseeld moet worden, moet deze while loop true worden
  coinValue = coinValues.pop(0) # Het laatst gebruikte muntgeld dat gebruikt is kan worden teruggegeven
  nrCoins = change // coinValue # Dit is het aantal ... munten dat teruggegeven moet worden aan de klant
  if nrCoins > 0: # Zodra het aantal munten minimaal 1 is of meer zal dit uitgevoerd worden
    print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # Dit is de reactie waarbij vertelt wordt met de hoeveelhei muntgeld muntjes er teruggegeven kan worden.
    nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # Hier staat hoeveel muntjes van bepaald muntgeld hebt teruggegeven aan de klant
    change -= nrCoinsReturned * coinValue # Dit is het wisselgeld dat nog teruggegeven moet worden.
    munt_soorten[coinValue] = nrCoinsReturned

# Hier wordt er een overzicht geprint van de hoeveelheid muntstukken er zijn teruggegeven
print(munt_soorten)

if change > 0: # Als er nog een restant wisselgeld is, dan zal er aangegeven worden hoeveel er nog niet teruggegeven is.
  print('Change not returned: ', str(change) + ' cents') 
else:
  print('done')