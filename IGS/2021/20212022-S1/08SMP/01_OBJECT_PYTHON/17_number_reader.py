import json

filename = "17_data.json"

with open(filename, "r") as data:
	animals = json.load(data)

for animal in animals:
	print(f"I have {animal}")