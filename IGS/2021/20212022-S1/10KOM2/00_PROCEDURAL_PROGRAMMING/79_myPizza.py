# topics : arbitrary arguments

def make_pizza(*toppings): # *args -> arguments
	print("\nMaking a pizza with the following toppings : ")
	"""
	Bermakna False: list kosong, string kosong, None, 0, dict kosong
	"""
	if toppings: # -> len(toppings) != 0
		for topping in toppings:
			print(f"\t- {topping}")
	else:
		print("There is no topping.")
	#print("Your Toppings :",toppings)

make_pizza()
make_pizza("cheese")
make_pizza("cheese", "mushrooms", "pepperoni") #tuple