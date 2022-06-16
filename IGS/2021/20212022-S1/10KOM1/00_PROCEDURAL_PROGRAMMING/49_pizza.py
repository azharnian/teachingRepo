#Nesting a list in a dictionary

pizza = {
	'crust' : 'thick',
	'toppings' : ['mushrooms', 'tomatoes', 'cheese', 'pineapple']
}

print(pizza['toppings'][1])

for topping in pizza['toppings']:
	print(f"\t{topping}")