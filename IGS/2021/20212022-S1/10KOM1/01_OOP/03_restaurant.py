
class Restaurant:


	def __init__(self, name, type, take_away=True):
		self.name = name
		self.type = type
		self.take_away = take_away

	def describe_restaurant(self):
		print(f"{self.name} is serving {self.type} food.")

	def serve_customer(self, ticket_number):
		print(f"Now serving customer : {ticket_number}.")


hokben = Restaurant("Hokben", "Japanese")
sederhana  = Restaurant("Sederhana", "Padang", False)
mcd = Restaurant(type="Western", name="MCD")


hokben.describe_restaurant()
sederhana.describe_restaurant()

hokben.serve_customer(76)
mcd.serve_customer(100)