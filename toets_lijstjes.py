tafel_van = 13
lijst_getallen = [5, 12, 19, 27, 3]
huidige_getal = 1
for y in range(tafel_van):
    for x in range(1, 11):
        print(f"{x} X {huidige_getal} = {x * tafel_van}")
    huidige_getal += 1

# opgave 3
lijst_getallen.append(25)
print(lijst_getallen)

# opgave 4
print(len(lijst_getallen))

# opgave 5
print(lijst_getallen)
lijst_getallen.remove(12)
print(lijst_getallen)

# opgave 6
print(lijst_getallen)
print(lijst_getallen.pop(0))
print(lijst_getallen)

# opgave 7
print(lijst_getallen)
lijst_getallen.insert(0, 36)
print(lijst_getallen)

# opgave 8
nummers = 0
for getal in lijst_getallen:
    if getal > 10:
        nummers = nummers + getal 
print(nummers)

# opgave 9
print(lijst_getallen)
lijst_getallen.clear()
print(lijst_getallen)

# opgave 10
for z in range(1, 4):
    lijst_getallen.append(z)
print(lijst_getallen)

# opgave 11
for a in range(4, 41):
    lijst_getallen.append(a)
print(lijst_getallen)

# opgave 12
print(lijst_getallen.index(25))

# opgave 13
None

# opgave 14
lijst_2 = [1, "aap", 2, "apen", 3, "watermeloen"]