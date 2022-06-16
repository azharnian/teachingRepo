class decorator_class:

	def __init__(self, original_function):
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		print('wrapper executed before {}, with args : {}, and kwargs : {}'.format(self.original_function.__name__, args, kwargs))
		return self.original_function()



class decorator_method_class:


	@staticmethod
	def call(original_function):

		def wrapper_function(*args, **kwargs):
			print('wrapper executed before {}, with args : {}, and kwargs : {}'.format(original_function.__name__, args, kwargs))
			return original_function(*args, **kwargs)

		return wrapper_function


@decorator_method_class.call
def display():
	print("display function ran.")

@decorator_class
def display_class():
	print("display function ran.")


display()
display_class()
