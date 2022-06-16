import json

with open('data.json', 'w') as file:
	#json.dump(100, file)
	#json.dump("Anas Azhar", file)
	numbers = [3, 1, 4, 1, 5, 9]
	json.dump(numbers, file)# with json pls, move data from numbers to file (data.json)