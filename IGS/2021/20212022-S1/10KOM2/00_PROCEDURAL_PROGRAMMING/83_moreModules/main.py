"""
#import entire module
import pizza

#module_name.function_name()
pizza.make_pizza(12, "mushrooms", "peppers", "cheese")
"""

"""
#import spesific function
from pizza import make_pizza

make_pizza(12, "mushrooms", "peppers", "cheese")
"""
"""
#import spesific function with alias
from pizza import make_pizza as mp

mp(12, "mushrooms", "peppers", "cheese")
"""
"""
from pizza import * #all (asterisk)

make_pizza(12, "mushrooms", "peppers", "cheese")
make_payment(400000, 385000)

"""
import pizza as p

p.make_pizza(12, "mushrooms", "peppers", "cheese")
p.make_payment(400000, 385000)
