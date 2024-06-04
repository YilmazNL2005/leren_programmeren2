def dorp(getal):
    resultaat = ""
    for x in range(1, getal+1):
        resultaat += f"Hello from function town {x}! \n"
    return resultaat

hello = dorp(7)
print(hello)