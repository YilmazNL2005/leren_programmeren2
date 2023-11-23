# example:
def increment(nr: float) -> float:
  return nr + 1

def decrement(nr: float) -> float:
  return nr - 1

def add(nr: float, nr2: float) -> float:
  return nr + nr2

def substract(nr: float, nr2: float) -> float:
  return nr2 - nr

def multiply(nr: float, nr2: float) -> float:
  return nr * nr2

def divide(nr: float, nr2: float) -> float:
  try:
    berekening = nr / nr2
    return berekening
  except ZeroDivisionError:
      berekening = None
      return berekening

# bom plus bom = kaboem
# bliksem gedeeld door doodskop = 3
# doodskop X 3