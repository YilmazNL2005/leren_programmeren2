uren1 = 1
uren2 = 1
AM = "AM"
PM = "PM"

while uren1 <= 13 and uren2 <= 13:
    if uren1 <= 12:
        print(uren1, AM)
        uren1 += 1
    else:
        if uren2 <= 11:
            print(uren2, PM)
            uren2 += 1
        else:
            uren1 = 12
            print(uren1, AM)
            break