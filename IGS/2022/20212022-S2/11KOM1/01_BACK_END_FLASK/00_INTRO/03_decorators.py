

def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print('wrapper executed this before {}'.format(original_function.__name__))
		return original_function(*args, **kwargs)
	return wrapper_function

@decorator_function
def display():
	print('display function ran well.')

@decorator_function
def display_info(name, age, school):
	print('display_info ran with argumens ({} {} {})'.format(name, age, school))

# decorator_function(display)
display()
display_info("Mike", 10, school="igs")

