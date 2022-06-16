# topics : regular and arbitrary arguments

def make_pizza(size, spice="hot", *toppings): # *args -> arguments
	print(f"\nMaking a {spice} {size} cm pizza with the following toppings : ")
	"""
	Bermakna False: list kosong, string kosong, None, 0, dict kosong
	"""
	if toppings: # -> len(toppings) != 0
		for topping in toppings:
			print(f"\t- {topping}")
	else:
		print("There is no topping.")
	#print("Your Toppings :",toppings)

make_pizza(12)
make_pizza(15, "extra chili", "cheese")
make_pizza(18, "not hot", "cheese", "mushrooms", "pepperoni") #tuple