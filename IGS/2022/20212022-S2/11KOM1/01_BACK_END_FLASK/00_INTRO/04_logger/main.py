
def my_logger(original_function):

	import logging

	logging.basicConfig(filename='{}.log'.format(original_function.__name__), level=logging.INFO)

	def wrapper(*args, **kwargs):
		logging.info('Ran with args : {} and kwargs {}'.format(args, kwargs))
		return original_function(*args, **kwargs)

	return wrapper

@my_logger
def display_info(name, age, school="IGS Palembang"):
	print('display_info ran with argumens ({} {} {})'.format(name, age, school))

@my_logger
def display_something(*args, **kwargs):
	print("DONE!")

# display_info("Kevin", 10)
display_something("1px", "solid", "Black", margin="10px")
