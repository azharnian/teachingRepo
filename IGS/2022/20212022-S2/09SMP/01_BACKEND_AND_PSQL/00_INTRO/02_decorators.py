
def decorator_function(original_function):

	def wrapper_function():
		print('wrapper executed before {}'.format(original_function.__name__))
		return original_function()

	return wrapper_function

@decorator_function
def display():
	print('display function ran well.')


display()