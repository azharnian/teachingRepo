

class Mouth:

	def __init__(self, HumanInfo):
		self.human = HumanInfo

	def describe_about_sex(self):
		print(f"I am {self.human.sex}")