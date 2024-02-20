from fruitmand import fruitmand

longest_name_fruit = 0
current_name_fruit = ""
current_color_fruit = ""
current_weight_fruit = 0

nl_kleuren = {
    "orange" : "oranje", 
    "red" : "rode", 
    "green" : "groene", 
    "yellow" : "gele", 
    "blue" : "blauwe", 
    "brown" : "bruine" 
}

for fruit in fruitmand:
    if len(fruit["name"]) > longest_name_fruit:
        longest_name_fruit = len(fruit["name"])
        current_name_fruit = fruit["name"]
        current_color_fruit = fruit["color"]
        current_weight_fruit = fruit["weight"]

current_color_fruit = nl_kleuren[current_color_fruit]
print(f"De {current_name_fruit} ({longest_name_fruit} Letters) heeft een {current_color_fruit} kleur en een gewicht van {current_weight_fruit / 1000} kg.")