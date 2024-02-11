import time
raket_aftelling = int(input("Vanaf hoeveel seconden wil je dat de raketlancering gaat? "))
while raket_aftelling > 0:
    print(f"Nog {raket_aftelling} seconden te gaan tot de raketlancering! ")
    raket_aftelling -= 1
    time.sleep(1)
print("De raket is gelanceerd!!!")