import os

user = ['barnie', '12345']
running = True
os.system('cls')

while running:
	username = input("Enter your username : ")
	password = input("Enter your password : ")

	if username == user[0] and password == user[1]:
		print("\nWELCOME")
		running = False
	else:
		print("\nPlease Try Again.")