from mouth import Mouth
from eye import Eye

class Head:

	def __init__(self, InfoHuman):
		self.eyes = Eye()
		self.mouth = Mouth(InfoHuman)