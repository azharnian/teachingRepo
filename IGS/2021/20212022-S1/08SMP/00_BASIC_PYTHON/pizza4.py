# passing an arbitrary number of arguments

def make_pizza(*toppings): # *args
	print(f"Making a {}-inch pizza with the following toppings :")
	for topping in toppings:
		print(f"- {topping}")

make_pizza('pinenapple') #tuple
make_pizza('mushrooms', 'red peppers', 'cheese') #tuple

# clue : for 
# Making a pizza with the following toppings :
# - pinenapple

# Making a pizza with the following toppings :
# - mushrooms
# - red peppers
# - cheese