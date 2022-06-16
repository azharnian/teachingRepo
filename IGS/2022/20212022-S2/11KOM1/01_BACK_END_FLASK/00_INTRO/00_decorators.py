
def outer_function(text):
	msg = text

	def inner_function():
		print(msg)

	return inner_function()


# inner_function("Hi!")
my_function = outer_function("Hi!")