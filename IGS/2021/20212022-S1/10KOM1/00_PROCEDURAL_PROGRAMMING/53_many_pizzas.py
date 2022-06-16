

pizzas = {
	"cheeseburger" : {
		"ingridients" : ["daging sapi cincang berbumbu", "keju cheddar", "saus mustard", "keju mozarella"],
		"price" : 100_000
	},
	"meat lovers" : {
		"ingridients" : ["sosis sapi", "daging sapi cincang", "burger sapi", "sosis ayam", "keju mozarella"],
		"price" : 0
	}
}

for pizza, info in pizzas.items():

	print(f"\n{pizza.title()}")

	for a_info, data in info.items():

		print(f"\t{a_info}")
		if type(data) == list:
			for item in data:
				print(f"\t\t- {item}")

		else:
			print(f"\t\t{data}")

	print()

