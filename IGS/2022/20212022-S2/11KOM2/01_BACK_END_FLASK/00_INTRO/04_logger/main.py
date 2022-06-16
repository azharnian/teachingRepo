


def my_logger(original_function):
	from datetime import datetime
	import logging

	logging.basicConfig(filename=f'{original_function.__name__}.log', level=logging.INFO)

	def wrapper(*args, **kwargs):
		today = datetime.now()
		logging.info(f'{today} - Ran with args : {args}, kwargs : {kwargs}')
		return original_function(*args, **kwargs)

	return wrapper

@my_logger
def display_info(customer, payment):
	print(f"This customer : {customer} had been paid {payment}.")

customer = input("Customer Name : ")
purchase = input("Purchase : ")
display_info(customer, purchase)