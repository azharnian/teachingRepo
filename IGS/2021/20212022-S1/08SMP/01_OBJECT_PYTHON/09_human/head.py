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