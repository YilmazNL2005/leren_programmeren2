import time
aftelling = int(input("Vanaf welk getal moet er afgeteld worden? "))
for x in range(aftelling, 0, -1 ):
    print(f"Raket stijgt op in {x} seconden")
    time.sleep(1)
print("Raket is gelanceerd!!!")