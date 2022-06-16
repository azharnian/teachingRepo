def make_pizza(size, *toppings):
	print(f"\nMaking a {size}cm pizza with the following toppings:")
	for topping in toppings:
		print(f"\t- {topping}")

def make_payment(money, purchased):
	print(f"\nHere is your payment : {money}")
	print(f"Your change : {money-purchased}")