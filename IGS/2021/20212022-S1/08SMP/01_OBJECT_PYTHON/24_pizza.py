#nesting a list in dictionary

pizza = {
	'crust' : 'thick',
	'toppings' : ['pineapple', 'tomato', 'cheese']
}

print(f"This pizza has a {pizza['crust']} crust.\nToppings : ")
for topping in pizza['toppings']:
	print(f"\t{topping}")