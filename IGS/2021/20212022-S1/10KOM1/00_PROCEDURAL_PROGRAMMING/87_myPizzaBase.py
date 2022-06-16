
#keywords arbitrary arguments

def make_pizza(**dough):
	print(f"\n Making a pizza with the following toppings:")
	print(dough)

def make_premium_pizza(size, *toppings, **dough): # *args, **kwargs
	print(f"\n Making a {size}cm pizza with the following toppings:")
	if toppings: 
		for topping in toppings:
			print(f"\t-{topping}")
	else:
		print("No topping.")
	if dough:
		print()
		for key, val in dough.items():
			print(key,val)

make_pizza(thickness="thick")
make_pizza(thickness="thin", size=20)
make_pizza()

make_premium_pizza(12, "cheese", "pepperoni", thickness="thick", crust=True)