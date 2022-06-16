
available_toppings = ['mushroom', 'cheese', 'pineapple', 'pepperoni']

requested_toppings = []

stop = False

while not stop:
	topping = input("Input your topping here ('q' to quit): ")
	if topping != 'q':
		requested_toppings.append(topping)
	else:
		stop = True


for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print(f"\nFinished making your pizza...")