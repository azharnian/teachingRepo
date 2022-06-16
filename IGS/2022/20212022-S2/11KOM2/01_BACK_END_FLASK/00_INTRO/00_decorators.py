def outer_function():
	msg = "Hi"

	def inner_function():
		print(msg)

	return inner_function()


my_function = outer_function()