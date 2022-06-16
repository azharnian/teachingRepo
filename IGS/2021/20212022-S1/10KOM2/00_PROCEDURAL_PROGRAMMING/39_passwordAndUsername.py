import getpass
import os

correct_username = "budi"
correct_password = "12345"

auth = False
os.system("cls")
while not auth:
	username = input("Masukkan username : ")
	password = getpass.getpass("Masukkan password : ")
	if username == correct_username and password == correct_password:
		print("Welcome")
		auth = True
	else:
		print("Username atau password tidak cocok, Coba lagi.")

