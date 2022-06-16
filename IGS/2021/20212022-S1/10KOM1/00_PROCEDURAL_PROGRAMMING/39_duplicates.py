

daftarAngka = [7, 8, 5, 1, 3, 3, 7, 8, 0, 2, 10]
daftarAngka.sort()

prev = None
for angka in daftarAngka:
	if angka == prev:
		print(f"Angka {angka} duplikat!")
	prev = angka

