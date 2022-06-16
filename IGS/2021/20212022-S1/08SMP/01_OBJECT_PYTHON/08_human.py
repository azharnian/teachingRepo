
class Head:

	def __init__(self, thisHuman):
		self.thisHuman = thisHuman
		self.eyes = 2
		self.mouth = 1
		self.nose = 1
		self.ears = 2
		self.hair = True
		self.hair_color = "Black"

	def tell_about_number_of_eyes(self):
		print("Number of Eyes : ", self.eyes)

	def describe_me_with_mouth(self):
		print(f"Hello, I'm {self.thisHuman.name}, {self.thisHuman.age} years old.")

class Body:

	def __init__(self):
		pass


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