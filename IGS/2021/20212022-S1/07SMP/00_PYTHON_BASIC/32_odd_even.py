
angka = int(input("Mulai dari = "))
stop = int(input("Berhenti sampai = "))
while angka <= stop:
	if angka % 2 == 0:
		print(f"{angka} Genap")
	else:
		print(f"{angka} Ganjil")
	angka += 1

"""
1 Ganjil
2 Genap
3 Ganjil
4 Genap
...
"""