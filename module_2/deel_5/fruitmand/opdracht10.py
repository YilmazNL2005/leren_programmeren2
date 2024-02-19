from fruitmand import fruitmand
from operator import itemgetter

# lijst = sorted(fruitmand, key=lambda d: d["weight"])
# lijst = sorted(fruitmand, key=itemgetter("weight"))
lijst = sorted(fruitmand, key=itemgetter("weight"), reverse=True)
fruitmand = lijst
for fruit in fruitmand:
    print(fruit["weight"], "gram")