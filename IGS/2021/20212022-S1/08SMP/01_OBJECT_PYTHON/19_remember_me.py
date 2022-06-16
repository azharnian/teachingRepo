import json

def greet_user():

	filename = "18_data.json"
	try:
		with open(filename, 'r') as data: #r -> read
			username = json.load(data)
	except json.decoder.JSONDecodeError:
		username = input("What is your name? ")

		with open("18_data.json", 'w') as data:
			json.dump(username, data)
			print(f"We'll remember you when you come back, {username}.")
			
	else:
		print(f"Welcome back, {username}")

def get_stored_username():
	pass

def get_new_username():
	pass


greet_user()