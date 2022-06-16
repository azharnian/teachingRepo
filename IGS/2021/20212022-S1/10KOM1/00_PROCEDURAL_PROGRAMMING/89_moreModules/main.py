"""
# import entire pizza
import pizza

pizza.make_pizza(12, "mushrooms")

# import spesific func
from pizza import make_pizza, make_payment

make_pizza(12, "mushrooms")


#import specific func with alias
from pizza import make_pizza as mp

mp(12, "mushrooms")

from pizza import * #all asterisk

make_pizza(12, "mushrooms")
"""
import pizza as p
p.make_pizza(12, "mushrooms")
