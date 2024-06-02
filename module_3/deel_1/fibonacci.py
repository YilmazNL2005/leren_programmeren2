# Dit moeten de uikomsten worden 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 

def fibonacci(a, b):
    for x in range(1,10+1):
        berekening = a + b
        a = b
        b = berekening
        print(f"{a} + {b} = {a + b}")

fibonacci(0, 1)