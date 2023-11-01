STUDIEDOKTER_TITEL = '''
*********************** STUDIEADVIES ***********************
Ik ga jou helpen met jouw opleiding. Jij krijgt een aantal stellingen te zien.
Voor elke stelling moet je zeggen hoeveel dat bij jou voorkomt. Je kunt steeds 
antwoorden: 0 is 'altijd'; 1 is 'vaak'; 2 is 'regelmatig'; 3 is 'soms'; 4 is 'nooit'.
Het is belangrijk om eerlijk te zijn. Op basis van jouw antwoorden krijg je advies. 
'''
OPTIES = "Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit"
AANTAL_WEKEN_VRAAG = 'Hoeveel weken ben je al bezig met de opleiding?'
COMPETENTIE_STELLING_1 = 'Ik voel stress of blokkades bij het maken van programmeeropdrachten.'
COMPETENTIE_STELLING_2 = 'Ik stel programmeeropdrachten en -uitdagingen uit.'
COMPETENTIE_STELLING_3 = 'Ik denk dat ik geen talent heb voor de opleiding.'
COMPETENTIE_STELLING_4 = 'Ik vermijd assessments (CJV) en feedback van kritische docenten. '
COMPETENTIE_STELLING_5 = 'Ik vergelijk mezelf met anderen die beter lijken te zijn.'
COMPETENTIE_STELLING_6 = 'Ik voel geen interesse in nieuwe programmeertechnieken.'
COMPETENTIE_STELLING_7 = 'Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is.'
aantal_weken = int(input("Hoeveel weken studeer je nu?"))

print(OPTIES)
vraag_1 = int(input(COMPETENTIE_STELLING_1))
vraag_2 = int(input(COMPETENTIE_STELLING_2))
vraag_3 = int(input(COMPETENTIE_STELLING_3))
vraag_4 = int(input(COMPETENTIE_STELLING_4))
vraag_5 = int(input(COMPETENTIE_STELLING_5))
if aantal_weken >= 10:
    vraag_6 = int(input(COMPETENTIE_STELLING_6))
    vraag_7 = int(input(COMPETENTIE_STELLING_7))
    vragen = [vraag_1, vraag_2, vraag_3, vraag_4, vraag_5, vraag_6, vraag_7]
else:
    vraag_6 = 0
    vraag_7 = 0
    vragen = [vraag_1, vraag_2, vraag_3, vraag_4, vraag_5]
print(OPTIES)

punten = vraag_1 + vraag_2 + vraag_3 + vraag_4 + vraag_5 + vraag_6 + vraag_7
print(punten)

stellingen = [COMPETENTIE_STELLING_1, COMPETENTIE_STELLING_2, COMPETENTIE_STELLING_3, COMPETENTIE_STELLING_4, COMPETENTIE_STELLING_5, COMPETENTIE_STELLING_6, COMPETENTIE_STELLING_7]
# vragen = [vraag_1, vraag_2, vraag_3, vraag_4, vraag_5, vraag_6, vraag_7]
# vragen.remove(vraag_6)
# vragen.remove(vraag_7)




COMPETENTIE_ADVIES_TITEL = '''
*********************** STUDIEADVIES ***********************'''
COMPETENTIE_ADVIES_ZORGELIJK = '''
Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart 
in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad 
op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen.
'''
COMPETENTIE_ADVIES_TWIJFELACHTIG = '''
Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaart
in het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!
'''
COMPETENTIE_ADVIES_GERUSTSTELLEND = '''
Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart in
het leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!
'''
gemiddelde_score = punten / len(vragen)
exacte_score = round(gemiddelde_score, 0)


print(gemiddelde_score)
print(exacte_score)
if exacte_score < 0:
    exacte_score = 0
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)
    print(exacte_score)
elif exacte_score == 2:
    print(COMPETENTIE_ADVIES_ZORGELIJK)
    print(exacte_score)
else:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
    print(exacte_score)