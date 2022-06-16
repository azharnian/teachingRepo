import os

def cetak_menu():
	print("*******************************")
	print("1. Lihat daftar nama")
	print("2. Tambah nama ke daftar")
	print("3. Hapus nama dari daftar")
	print("4. Ubah/Perbarui nama di daftar")
	print("Q. Keluar dari program")
	print("*******************************")

def lihat_daftar_nama():
	os.system("clear") # windows -> cls
	print("-DAFTAR NAMA-")
	if len(daftarNama) > 0:
		index = 0
		while index < len(daftarNama):
			print(index, ".", daftarNama[index])
			index += 1
	else:
		print("Daftar Nama Kosong")
	input("Tekan ENTER untuk kembali ke MENU")

def tambah_nama():
	os.system("clear") # windows -> cls
	print("-TAMBAH NAMA-")
	nama_baru = input("Masukkan nama yang akan ditambah : ")
	if len(nama_baru) > 0:
		daftarNama.append(nama_baru)
		print("Nama tersimpan!")
	else:
		print("Nama tidak boleh kosong!")
	input("Tekan ENTER untuk kembali ke MENU")

def hapus_nama():
	os.system("clear") # windows -> cls
	print("-HAPUS NAMA-")
	nama_dihapus = input("Masukkan nama yang akan dihapus : ")
	if nama_dihapus in daftarNama:
		daftarNama.remove(nama_dihapus)
		print("Nama telah dihapus!")
	else:
		print("Nama tidak ditemukan!")
	input("Tekan ENTER untuk kembali ke MENU")

def perbarui_nama():
	pass

daftarNama = ["anas", "budi"]
pilihan = None
error = False

while not error:

	cetak_menu()

	pilihan = input("Pilih Menu : ")

	if pilihan == "1":
		lihat_daftar_nama()
	elif pilihan == "2":
		tambah_nama()
	elif pilihan == "3":
		hapus_nama()
	elif pilihan == "4":
		perbarui_nama()
	elif pilihan == "Q":
		error = True