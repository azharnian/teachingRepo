
def make_pizza(size, *toppings):
	print(f"\n Making {size}cm pizza with the following toppings:")
	if toppings:
		for topping in toppings:
			print(f"\t-{topping}")
	else:
		print("No topping.")

def make_payment(money, purchased):
	print(f"your change : {money-purchased}")