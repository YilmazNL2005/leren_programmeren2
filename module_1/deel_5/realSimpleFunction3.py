import math
from test_lib import test, report 

month_discount_brands = 'Vespa,Kymco,Yamama'
MONTH_DISCOUNT_PERC = 10

def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    discount_brands = month_discount_brands.split(',')
    
    if brand in discount_brands:
        discount = (price * MONTH_DISCOUNT_PERC) / 100
    else:
        discount = 0.0
    
    return round(discount, 2)

# Testgevallen
test(name="Test 1", expect=calc_discount(100, 'Vespa', month_discount_brands), value=10.00)
test(name="Test 2", expect=calc_discount(150, 'Kymco', month_discount_brands), value=15.00)
test(name="Test 3", expect=calc_discount(200, 'Yamama', month_discount_brands), value=20.00)
test(name="Test 4", expect=calc_discount(120, 'Honda', month_discount_brands), value=0.00)
test(name="Test 5", expect=calc_discount(80, 'Yamama', 'Piaggio,Sym,Yamama'), value=8.00)


report()


# def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
#     # return calculated discount based on price and brand



# month_discount_brands = 'Vespa,Kymco,Yamama'
# MONTH_DISCOUNT_PERC = 10
