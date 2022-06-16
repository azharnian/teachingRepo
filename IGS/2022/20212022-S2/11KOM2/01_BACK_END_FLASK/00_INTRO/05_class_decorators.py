

class decorator_class:

	def __init__(self, original_function):
		self.original_function = original_function


	def __call__(self, *args, **kwargs):
		print(f"call method excuted before {self.original_function.__name__}")
		return self.original_function()

@decorator_class
def display():
	print("display function ran ...")

display()