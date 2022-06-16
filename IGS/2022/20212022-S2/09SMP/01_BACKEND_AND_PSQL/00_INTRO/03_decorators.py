
def decorator_function(original_function):

	def wrapper_function(*args, **kwargs):
		print('wrapper executed before {}, with args : {}, and kwargs : {}'.format(original_function.__name__, args, kwargs))
		return original_function(*args, **kwargs)

	return wrapper_function

@decorator_function
def display():
	print('display function ran well.')

@decorator_function
def display_info(name, age):
	print(f'display_info ran with arguments ({name}, {age})')

@decorator_function
def display_things(name, age, school):
	print(f"display_things ran with arguments ({name}, {age}, {school})")

display()
display_info("Kevin", 20)
display_things("Vincent", school="IGS", age=20)