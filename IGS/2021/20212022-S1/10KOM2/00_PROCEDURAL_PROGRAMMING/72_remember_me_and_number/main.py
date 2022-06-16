import json
import random

def load_data():
	try:
		with open("data.json", "r") as file:
			return json.load(file)
	except:
		return {} # {} != None

def save_data(data_master):
	with open("data.json", "w") as file:
		json.dump(data_master, file)
		return True

def greet_user(data_master):
	username = input("What is your name ? ")
	if username in data_master:
		print(f"Welcome back {username}!")
	else:
		data_master[username] = None
		save_data(data_master)
		print("We'll remember you when you come back!")
	return username

def get_new_favorite_number(guessing_number):
	ans = input(f"I'll guess your favorite number is {guessing_number}, is it right ? (y/n) ")
	if ans.lower() == "y":
		return guessing_number
	elif ans.lower() == "n":
		return int(input("So, what is your favorite ? "))
		#2 handling error kalau user tidak kasih masukan integer
	else:
		print("please, answer with y or n! ")
		return get_new_favorite_number(guessing_number)

def ask_user(data_master, username):
	#print(data_master, username)
	if username in data_master:
		if data_master[username]:
			print(f"I know your favorite number, it is {data_master[username]}")
			#1 tawaran mau ubah favorite numbernya ga ?
		else:
			guessing_number = random.randint(0, 100)
			favorite_number = get_new_favorite_number(guessing_number)
			data_master[username] = favorite_number
			save_data(data_master)
			print("We'll remember your favorite number next time.")


data_master = load_data()
ask_user(data_master, greet_user(data_master))