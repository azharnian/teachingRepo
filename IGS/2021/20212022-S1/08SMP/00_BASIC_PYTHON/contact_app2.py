import os
import sys
from getpass import getpass


def security_login():
	login = False
	limit_login_attemp = 0

	while not login:
		os.system("clear") #"cls"
		if limit_login_attemp >= 3:
			print('Your Login Attempt Reach Limit')
			break

		username_input = input("USERNAME : ")
		password_input = getpass("PASSWORD : ")

		if username_input == user['username'] and password_input == user['password']:
			print('Welcome!')
			login = True
		else:
			limit_login_attemp += 1
			print('Login Failed, Try Again!')
	else:
		return True
	return False

def view_menu():
	os.system("clear") #"cls"
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

def print_contacts():
	os.system("clear") #"cls"
	print("\nDaftar Kontak\n ======= \n")
	print("Nomor HP\t|\tNama\t|\tAlamat\n")

	for phone_number, info_contact in contacts.items():

		print(f"{phone_number}\t|\t{info_contact['f_name'].title()}\t|\t{info_contact['address']}")
	input("Tekan ENTER untuk kembali ke MENU UTAMA")

def add_contact():
	os.system("clear")
	print("\nTambah Kontak Baru\n ====== \n")
	f_name = input("Nama Depan\t: ")
	l_name = input("Nama Belakang\t: ")
	phone = input("Nomor HP\t: ")
	address = input("Alamat\t: ")
	confirmed = input("Yakin kontak ini akan disimpan ? (y/n) ")
	if confirmed == "y":
		contacts[phone] = {
			"f_name" : f_name,
			"l_name" : l_name,
			"address" : address
		}
		print("Kontak Telah Disimpan")
	else:
		print("Batal Disimpan")
	input("Tekan ENTER untuk kembali ke MENU UTAMA")	

def print_detail_contact(phone, info):
	print("Kontak Ditemukan\n")
	print(f"Nomor Telp\t: {phone}")
	print(f"Nama Lengkap\t: {info['f_name']} {info['l_name']}")
	print(f"Alamat\t: {info['address']}")

def searching_contact(search_item):
	for phone, info in contacts.items(): #key = phone, value = info
		if search_item in phone:
			print_detail_contact(phone, info)
			return phone
		elif search_item in info['f_name']:
			print_detail_contact(phone, info)
			return phone
		elif search_item in info['l_name']:
			print_detail_contact(phone, info)
			return phone
	else:
		print("Kontak Tidak Ditemukan.")
		return None

def search_contact(): #subroutine
	os.system("clear") #'cls'
	print("Cari Kontak\n")
	search_item = input('Masukkan input pencarian : ')
	key_contact = searching_contact(search_item)
	input("Tekan ENTER untuk kembali ke MENU UTAMA")

def update_contact():
	pass

def delete_contact():
	os.system("clear") #'cls'
	print("Hapus Kontak\n")
	search_item = input('Masukkan input kontak yang akan dihapus : ')
	key_contact = searching_contact(search_item)
	if key_contact:
		confirmed = input("Yakin kontak ini mau dihapus ? (y/n) ")
		if confirmed == "y":
			del contacts[key_contact]
			print("Kontak Telah Dihapus.")
	input("Tekan ENTER untuk kembali ke MENU UTAMA")


def about_application():
	pass

def check_input(user_input):
	if user_input == "1":
		print_contacts()
	elif user_input == "2":
		add_contact()
	elif user_input == "3":
		search_contact()
	elif user_input == "4":
		update_contact()
	elif user_input == "5":
		delete_contact()
	elif user_input == "6":
		about_application()
	elif user_input == "Q":
		print("Good Bye Howdy ...!")
		# running = False
		sys.exit()

user = {
	"username" : "admin",
	"password" : "12345"
}

contacts = {
	"081122334455" : {
		"f_name" : "Budi",
		"l_name" : "Santoso",
		"address" : "Kenten"
	},
	"082233445566" : {
		"f_name" : "Cindy",
		"l_name" : "Situmorang",
		"address" : "Kuto"
	}
}

running = True #security_login()
while running:
	view_menu()
	user_input = input("Pilihan Menu : ").upper()
	check_input(user_input)
	



