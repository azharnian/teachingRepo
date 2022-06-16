# ==, !=, >, <, >=, <=

daftarAngka = [7, 8, 5, 1, 3, 3, 5, 7]
daftarAngka.sort()
prev = None
for angka in daftarAngka:
	if prev == angka:
		print(f"Angka {angka} duplikat.")
	prev = angka