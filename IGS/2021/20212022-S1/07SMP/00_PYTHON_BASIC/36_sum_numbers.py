angka_sekarang = 0
angka_dijumlahkan = 0

while True:
	angka_dijumlahkan += angka_sekarang
	print(angka_dijumlahkan)
	angka_sekarang = int(input("Angkanya ? "))
	if angka_sekarang == 0:
		break
print(f"Jumlah semua angka = {angka_dijumlahkan}")