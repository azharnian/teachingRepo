import os

def print_menu():
	print("1. Lihat daftar nama\n2. Tambah nama ke daftar\n3. Hapus nama dari daftar\n4. Ubah nama di daftar\n0. Keluar")

def lihat_daftar_nama():
	os.system("clear")
	print("-DAFTAR NAMA-")
	for nama in daftar_nama:
		print(nama)
	input("Tekan ENTER untuk kembali ke MENU UTAMA.")


def tambah_daftar_nama():
	os.system("clear")
	print("-TAMBAH NAMA-")
	nama = input("Masukkan nama baru : ")
	respons = input(f"Kamu yakin ingin menambahkan {nama} ? (y/n) ")

	if respons == "y":
		daftar_nama.append(nama)
		print("Nama telah disimpan.")
	else:
		print("Nama batal disiimpan")

	input("Tekan ENTER untuk kembali ke MENU UTAMA.")


def hapus_nama():
	os.system("clear")
	print("-HAPUS NAMA-")
	nama = input("Masukkan nama yang akan dihapus : ")
	if nama in daftar_nama:
		respons = input(f"Nama {nama} ditemukan, yakin dihapus ?(y/n) ")
		if respons == "y":
			daftar_nama.remove(nama)
			print("Nama telah dihapus.")
		else:
			print("Nama batal dihapus")
	else:
		print("Nama tidak ditemukan.")

	input("Tekan ENTER untuk kembali ke MENU UTAMA.")


def ubah_nama():
	os.system("clear")
	print("-UBAH NAMA-")
	nama = input("Masukkan nama yang akan diubah ? ")
	if nama in daftar_nama:
		print(f"Nama {nama} ditemukan.")
		nama_baru = input("Masukkan nama baru : ")
		respons = input(f"Yakin mengubah nama {nama} menjadi {nama_baru} ? (y/n)")
		if respons == "y":
			daftar_nama[daftar_nama.index(nama)] = nama_baru
			print("Nama telah diubah.")
		else:
			print("Nama batal diubah.")
	else:
		print("Nama tidak ditemukan.")

	input("Tekan ENTER untuk kembali ke MENU UTAMA.")


daftar_nama = ["anas", "budi"]
pilihan = None
error = False

while not error:
	os.system("clear") #windows cls
	print_menu()

	pilihan = input("Pilih Menu : ")
	if pilihan == "0":
		error = True
	elif pilihan == "1":
		lihat_daftar_nama()
	elif pilihan == "2":
		tambah_daftar_nama()
	elif pilihan == "3":
		hapus_nama()
	elif pilihan == "4":
		ubah_nama()






		
