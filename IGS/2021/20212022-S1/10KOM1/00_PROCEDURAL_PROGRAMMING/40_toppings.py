

req_toppings = ['mushroom', 'cheese', 'pineapple', 'pepperoni']

req_customer = input('Add your topping : ')

if req_customer in req_toppings:
	print(f"Adding {req_customer.title()} and making your pizza.")
else:
	print(f"Sorry, we are out of {req_customer.title()} right now.")

