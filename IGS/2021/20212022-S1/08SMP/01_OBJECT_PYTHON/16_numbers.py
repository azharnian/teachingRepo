import json
numbers = [3, 4, 5, 7, 1, 0, 9]

filename = '16_data.json' #xml
with open(filename, 'w') as data:
	json.dump(numbers, data)