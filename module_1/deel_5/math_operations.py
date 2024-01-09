# example:
def increment(nr: float) -> float:
  return nr + 1

def decrement(nr: float) -> float:
  return nr - 1

def add(nr: float, nr2: float) -> float:
  return nr + nr2

def substract(nr: float, nr2: float) -> float:
  return nr - nr2

def multiply(nr: float, nr2: float) -> float:
  return nr * nr2

def divide(nr: float, nr2: float) -> float:
  try:
    berekening = nr / nr2
    return berekening
  except ZeroDivisionError:
      berekening = None
      return berekening

def min_max(nr1: float, nr2: float) -> str:
  maximum = max(nr1,nr2)
  minimum = min(nr1,nr2)
  if nr1 < nr2:
    maximum,minimum = minimum,maximum
  return f'maximum: {maximum} en minimum: {minimum}'






# if nr1 < nr2:
#   nr1,nr2 = nr2,nr1
#   return 
# elif nr1 > nr2:
#   return f'Maximum: {nr1} en minimum: {nr2}'
# else:
#   return 'Beide getallen zijn even groot'

# Definieer een function:
# met een duidelijke naam en alle type aanduidingen
# Met 2 parameters voor twee int getallen: nr1 en nr2
# Returnt de string: 'Beide getallen zijn even groot’, als nr1 en nr2 even groot blijken te zijn
# Returnt de string: f'Maximum: {nr1} en minimum: {nr2}’ als nr1 groter is
# Returnt de string: f'Maximum: {nr2} en minimum: {nr1}’ als nr2 groter is
# Test voor de 3 gevallen! Gebruik test_lib.py





# bom plus bom = kaboem
# bliksem gedeeld door doodskop = 3
# doodskop X 3