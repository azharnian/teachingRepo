

def decorator_function(original_function):

	def wrapper_function(*args, **kwargs):
		print('wrapper executed this before {} function'.format(original_function.__name__))
		print(f'args : {args}, kwargs : {kwargs}')
		return original_function(*args, **kwargs)

	return wrapper_function


@decorator_function
def display():
	print('display function ran well.')

@decorator_function
def display_info(name, age):
	print('display_info ran with arguments ({}, {})'.format(name, age))

@decorator_function
def display_something(name, age, school):
	print('display_info ran with arguments ({}, {}, {})'.format(name, age, school))


display_info("Kevin", 15)
display()
display_something("Vincent", school="IGS Palembang", age=100)