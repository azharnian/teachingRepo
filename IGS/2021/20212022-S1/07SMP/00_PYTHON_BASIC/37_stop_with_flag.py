angka_sekarang = 0
angka_dijumlahkan = 0
#stop = False # flag variable, penanda
playing = True

while playing: #not stop
	angka_dijumlahkan += angka_sekarang
	print(angka_dijumlahkan)
	angka_sekarang = int(input("Angkanya ? "))
	if angka_sekarang == 0:
		playing = False #stop = True
print(f"Jumlah semua angka = {angka_dijumlahkan}")