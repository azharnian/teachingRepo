
class Car:

	def __init__(self, merk, model, year, color="Black", isNew=True, isAutomatic=True): #default argument
		
		self.merk = merk
		self.model = model
		self.year = year
		self.color = color
		self.isNew = isNew # True/False
		self.isAutomatic = isAutomatic
		self.odometer = 0 # default attribute

	def get_descriptive_car(self):
		if self.isNew:
			condition = "New"
		else:
			condition = "Second"

		if self.isAutomatic:
			carType = "Matic"
		else:
			carType = "Manual"

		message = f"This car is a {self.merk}'s car.\nIts model is {self.model}-{self.year}.\nIt has {self.color} color.\nThe condition is {condition} and {carType} type."
		return message


my_car = Car(merk="Honda", model="CRV", year=2019, color="White", isNew=True, isAutomatic=True)
print(my_car.get_descriptive_car())

your_car = Car(merk="Toyota", model="Inova", year="2021")
print(your_car.get_descriptive_car())