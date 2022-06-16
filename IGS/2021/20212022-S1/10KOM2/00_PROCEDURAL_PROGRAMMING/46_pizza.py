#Nesting: A List in a dictionary

#menyimpan informasi tentang sebuah pizza
pizza = {
	'crust' : 'thick',
	'toppings' : ['mushrooms', 'cheese', 'pineapple']
}

print(pizza['toppings'][0])

for topping in pizza['toppings']:
	print(f"\t {topping}")