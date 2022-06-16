
def buat_indomie(porsi): # argument function
	print("1. Siapin Indomie dan telur (opsional)")
	print("2. Rebus Air")
	print("3. Tunggu air mendidih")
	print("4. Masukkan telur yang sudah dipecahkan")
	print("5. Masukkan mie yang sudah dibuka dari kemasan")
	harga = 5000 * porsi
	print("harganya : ",harga)
	return harga #None

print("harganya : ",buat_indomie(3)) # parameter