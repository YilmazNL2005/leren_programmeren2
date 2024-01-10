from garage import autolijst
print(f"Ik heb {len(autolijst)} auto's in mijn garage. ")
aantal_auto = 0
for auto in autolijst:
    if auto["automerk"] == "volkswagen":
        aantal_auto += 1

print(aantal_auto)

def getMotorInhoud(a):
    return a["motorinhoud"]

print(min(autolijst, key = getMotorInhoud))
print(min(autolijst, key = lambda a : a(getMotorInhoud)))