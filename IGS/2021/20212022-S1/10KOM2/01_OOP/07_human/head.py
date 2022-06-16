
from eye import Eye
from mouth import Mouth

class Head:

	def __init__(self, HumanInfo):
		self.human = HumanInfo
		self.eyes = Eye() #obj in obj atau obj as an attribute
		self.mouth = Mouth(self.human) #Mouth(HumanInfo)