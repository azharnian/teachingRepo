

req_toppings = ['mushroom', 'cheese', 'green peppers', 'pineapple']

req_customer = input("Add your topping : ")

if req_customer in req_toppings:
	print(f"Adding {req_customer} and making your pizza!")
else:
	print(f"Sorry, we are out of {req_customer} right now.")