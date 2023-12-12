# import random
# def generate_compliment(gegeven_naam: str) -> str:
#     complimenten = (f"Je bent goed bezig: {gegeven_naam}", f"Je hebt het super gedaan: {gegeven_naam}", f"Wat zie je er goed uit: {gegeven_naam}", f"Je bent geweldig: {gegeven_naam}", f"Je hebt een leuke naam: {gegeven_naam}")
#     gekozen_compliment = random.choice(complimenten)
#     return gekozen_compliment

# naam = input("wat is je naam? ")
# print(generate_compliment(naam)) # Argument
lijst = []
auto = {}
for x in range(3):
    auto["automerk"] = input("Wat is het automerk? ")
    auto["bouwjaar"] = float(input("Wat is het bouwjaar van de " + auto["automerk"][x] + " ? "))
    auto["aankoopprijs"] = float(input("Hoeveel kost de auto in euro's? "))
    lijst.append(auto)
    auto = {}
print(lijst)
