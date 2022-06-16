import os

def cetak_menu():
	os.system("clear")
	print("1. Lihat daftar belanja")
	print("2. Tambah barang ke daftar belanja")
	print("3. Hapus barang dari daftar belanja")
	print("4. Ubah/Perbarui barang di daftar belanja")
	print("Q. Keluar dari program")

def lihat_daftar_belanja():
	os.system("clear")
	print("Daftar Belanja")
	#print(daftarBelanja)
	if len(daftarBelanja) > 0:
		index = 0
		while index < len(daftarBelanja):
			print(index, ".", daftarBelanja[index])
			index += 1
	else:
		print("Belum Daftar Belanja.")
	input("Tekan ENTER untuk kembali ke MENU")

def tambah_barang():
	os.system("clear")
	print("Tambah Barang")
	barang_baru = input("Masukkan barang yang akan di tambah : ")
	if len(barang_baru) > 0:
		daftarBelanja.append(barang_baru)
		print("Barang sudah ditambahkan.")
	else:
		print("Barang tidak boleh kosong.")
	input("Tekan ENTER untuk kembali ke MENU")

def hapus_barang():
	os.system("clear")
	print("Hapus Barang")
	barang_dihapus = input("Masukkan barang yang akan dihapus : ")
	if barang_dihapus in daftarBelanja:
		daftarBelanja.remove(barang_dihapus)
		print("Barang sudah dihapus.")
	else:
		print("Barang tidak ditemukan.")
	input("Tekan ENTER untuk kembali ke MENU")

def ubah_barang():
	"""
	["a", "b", "c"]
	a -> d
	betul = ["d", "b", "c"]
	salah = ["b", "c", "d"]

	b -> d
	betul = ["a", "d", "c"]
	"""
	os.system("clear")
	print("Ubah Barang")
	barang_diubah = input("Masukkan barang yang akan diubah : ")
	if barang_diubah in daftarBelanja:
		index = daftarBelanja.index(barang_diubah)
		barang_baru = input("Masukkan barang barunya : ")
		daftarBelanja[index] = barang_baru
		print("Barang sudah diubah.")
	else:
		print("Barang tidak ditemukan.")
	input("Tekan ENTER untuk kembali ke MENU")


daftarBelanja = ["Chicken Katsu", "Wipol"]
pilihan = None

running = True

while running:

	cetak_menu()

	pilihan = input("Masukkan Pilihan Menu : ")
	if pilihan == "1":

		lihat_daftar_belanja()

	elif pilihan == "2":

		tambah_barang()

	elif pilihan == "3":
			
		hapus_barang()	

	elif pilihan == "4":
		
		ubah_barang()

	elif pilihan == "Q":
		running = False

print("Bye .. bye.. ")