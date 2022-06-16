

class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"{self.restaurant_name} is serving {self.cuisine_type} food.")

	def serve_customer(self, ticket_number):
		print(f"Now serving, customer : {ticket_number}")

hokben = Restaurant("Hokben", "Japanese")
sederhana = Restaurant("Sederhana", "Padang")

hokben.describe_restaurant()
sederhana.describe_restaurant()

hokben.serve_customer(98)