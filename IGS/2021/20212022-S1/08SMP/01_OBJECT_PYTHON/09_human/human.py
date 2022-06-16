# import head
# import body
from head import Head
from body import Body

class Human:

	def __init__(self, name, age, sex):

		self.name = name
		self.age = age
		self.sex = sex

		self.head = Head(self)
		self.body = Body()

	def describe_me(self):
		print(f"Hello, I'm {self.name}, {self.age} years old.")

	def tell_about_number_of_eyes(self):
		print("Number of Eyes : ", self.head.eyes)


ruliff = Human(name="Ruliff", age=13, sex="Male")
ruliff.describe_me()
print("Number of Eyes : ",ruliff.head.eyes)
ruliff.tell_about_number_of_eyes()
ruliff.head.tell_about_number_of_eyes()
ruliff.head.describe_me_with_mouth() # same with line 44