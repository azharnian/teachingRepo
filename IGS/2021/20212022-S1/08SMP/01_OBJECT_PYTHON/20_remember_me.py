#refactoring 20 -> 2*2*5 -> 2^2*5
# x^2y + xy -> xy(x+1)
import json

def greet_user():

	username = get_stored_username()
	if username:
		print(f"Welcome back, {username}")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}.")


def get_stored_username():
	filename = "18_data.json"
	try:
		with open(filename, 'r') as data: #r -> read
			username = json.load(data)
	except json.decoder.JSONDecodeError:
		return None			
	else:
		return username

def get_new_username():
	username = input("What is your name? ")
	with open("18_data.json", 'w') as data:
		json.dump(username, data)
	return username	


greet_user()