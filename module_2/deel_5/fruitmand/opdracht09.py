from fruitmand import fruitmand

print(fruitmand )
for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit)
print(fruitmand)

for fruit in fruitmand:
    print(fruit['name'])