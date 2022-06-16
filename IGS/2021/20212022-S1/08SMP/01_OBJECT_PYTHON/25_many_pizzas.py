#Nesting Dictionaries in a Dictionary

pizzas = {
	"cheeseburger" : {
		"ingridients" : ["Daging Sapi Cincang Berbumbu", "Keju Cheddar","Saus Mustard", "Keju Mozarella"],
		"price" : 100_000
	},
	"meat lovers" : {
		"ingridients" : ["Sosis Sapi", "Daging Sapi Cincang", "Burger Sapi", "Sosis Ayam", "Keju Mozarella"],
		"price" : 150_000
	}
}

for pizza, infos in pizzas.items():

	print(f"Pizza {pizza.title()}\n")

	for info, data in infos.items():

		if type(data) == list:
			print(f"\t{info.upper()} \t:")

			for item in data:
				print(f"\t\t> {item}")
		else:
			print(f"\t{info.upper()} \t: {data}")
	print()