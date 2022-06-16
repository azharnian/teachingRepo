# arbitrary arguments

def make_pizza(*toppings):
	print("\n Making pizza with the following toppings:")
	#print(toppings)
	#False : list kosong, string kosong, None, 0, dict kosong
	if toppings: # len(toppings) > 0
		for topping in toppings:
			print(f"\t-{topping}")
	else:
		print("No topping.")


make_pizza()
make_pizza("cheese")
make_pizza("cheese", "mushrooms", "pepperoni")