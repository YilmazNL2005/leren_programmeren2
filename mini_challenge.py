GETALLEN_REEKS = (2, 7, 18, 25, 24, 17, 420, 8, 3, 200)
even_getallen = []
for nummers in GETALLEN_REEKS:
    if nummers % 2 == 0:
        print(nummers)
        even_getallen.append(nummers)

print(len(even_getallen))

#Filter