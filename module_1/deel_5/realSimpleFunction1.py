from test_lib import test, report 
import math


def calculate_cilinder_content(diameter, hoogte):
    inhoud = (diameter/ 2) * (diameter/ 2) * math.pi * hoogte
    return round(inhoud,1)
antwoord = calculate_cilinder_content(8, 5)
print(antwoord)

diameter = 8.0
height = 5.0
expect_content = 251.3
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )

report()

diameter = 11.0
height = 7.0
expect_content = 251.3
calculated_content = calculate_cilinder_content(diameter,height)
name = f'test diameter: {diameter} height: {height}'
test(name, expect_content, calculated_content )

report()