"""
1.Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information.
2.Make an instances (object) from that class, and call the method.
3.Create three different instances from the class, and call describe_restaurant() for each instance.

"""

class Restaurant: #object class / template

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"{self.restaurant_name} is serving {self.cuisine_type} food.")

my_resto = Restaurant(restaurant_name="Hokben", cuisine_type="Japanese") # instance
my_resto.describe_restaurant()