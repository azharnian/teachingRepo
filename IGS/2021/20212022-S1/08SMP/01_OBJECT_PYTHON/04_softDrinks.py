

class SoftDrinks:

	def __init__(self, merk, size, flavor, exp_date, ingridients):

		self.merk = merk
		self.size = size
		self.flavor = flavor
		self.exp_date = exp_date
		self.ingridients = ingridients
		self.frozeness = 100


	def get_descriptive_drinks(self):

		message = f"{self.merk}\n{self.size} ml\n {self.flavor} flavor\nexp. date : {self.exp_date}\ningridients : {self.ingridients}"
		return message

my_tehGelas = SoftDrinks(merk="Teh Gelas", size=250, flavor="Just Tea and Sugar", exp_date="2022/03/03", ingridients="Tea Leaves, Sugar, Monosodium Glutamate, Natrium Hidroxide")
print(my_tehGelas.get_descriptive_drinks())