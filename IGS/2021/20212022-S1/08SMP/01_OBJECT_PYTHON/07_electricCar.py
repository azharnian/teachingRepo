#inheritance

class Car: #ElectricCar's Parent

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
	#modifying attributes through a method (function inside class)
	def change_merk(self, new_merk):
		self.merk = new_merk

	def increment_odometer(self, kms):
		self.odometer += kms
		print(f"The Odometer has been updated to {self.odometer}.")

	def fill_gas_tank(self):
		print("The Car is full of fuel right now.")

class ElectricCar(Car): #Car's Child
	
	def __init__(self, merk, model, year, color="Black", isNew=True, isAutomatic=True):
		super().__init__(merk, model, year, color, isNew, isAutomatic)
		self.battery_capacity = 100 #Special Attribute

	def get_descriptive_battery(self): #Special Method
		print(f"This car has a {self.battery_capacity}% Capacity")

	def fill_gas_tank(self): #overriding methods from parent class
		print("This car doesn't need a gas tank!")

class Bus(Car):
	pass
	# 1 special attribute
	# 1 special method

class ElectricBus(Bus):
	pass


my_tesla = ElectricCar('Tesla', 'Model S', '2019', color="White")
print(my_tesla.get_descriptive_car())
my_tesla.get_descriptive_battery()

transmusi = Bus()

transmusi_electric = ElectricBus()






