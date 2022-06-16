import os
from getpass import getpass

def view_menu():
	os.system("clear")
	menu = """
	-APLIKASI KONTAK KITA BERSAMA-
	1. Tampilkan Semua Kontak
	2. Tambah Kontak
	3. Cari Kontak
	4. Perbarui Kontak
	5. Hapus Kontak
	6. Tentang Aplikasi
	Q. Keluar
		"""
	print(menu)

def check_input(char):
	if char == "q":
		return True
	elif char == "1":
		pass
	elif char == "2":
		pass
	elif char == "3":
		pass

def check_login():
	global login_attemp
	username_input = input("username : ")
	password_input = getpass("password : ")

	while username_input != user["username"] or password_input != user["password"]:
		login_attemp += 1
		print("Try Again!")
		username_input = input("username : ")
		password_input = getpass("password : ")
		if login_attemp == 3:
			return False
	else:
		print("WELCOME CAPT!")
		return True

###PROGRAM UTAMA

user = {
	"username" : "admin",
	"password" : "12345"
}

login_attemp = 0
approved = False
stop = False

approved = check_login()
if approved:
	while not stop:
		view_menu()
		user_input = input("Pilihan : ").lower()
		stop = check_input(user_input)

else:
	print('Failed To Login')