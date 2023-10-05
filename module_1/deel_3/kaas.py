kaas_geel = input("Is de kaas geel? ")
if kaas_geel == "ja":
    kaas_gaten = input("Zitten er gaten in? ")
    if kaas_gaten == "ja":
        dure_kaas = input("Is de kaas belachelijk duur? ")
        if dure_kaas == "ja":
            print("Emmenthaler")
        elif dure_kaas == "nee":
            print("Leerdammer")
    elif kaas_gaten == "nee":
        harde_kaas = input("Is de kaas hard als steen? ")
        if harde_kaas == "ja":
            print("Parmigiano Reggiano")
        elif harde_kaas == "nee":
            print("Goudse kaas")
elif kaas_geel == "nee":
    blauwe_schimmel = input("Heeft de kaas blauwe schimmel? ")
    if blauwe_schimmel == "ja":
        korst_kaas = input("Heeft de kaas korst? ")
        if korst_kaas == "ja":
            print("Blue de Rochbaron")
        elif korst_kaas == "nee":
            print("Foume d'ambert")
    elif blauwe_schimmel == "nee":
        korst_kaas = input("Heeft de kaas korst? ")
        if korst_kaas == "ja":
            print("Camenbert")
        elif korst_kaas == "nee":
            print("Mozzarella")