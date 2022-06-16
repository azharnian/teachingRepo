import random

angkaBenar = random.randint(0,100)
tebakan = None

print("Tebak Angka!\n")
while tebakan != angkaBenar:
	tebakan = int(input("Angkanya : "))

	if tebakan == angkaBenar:
		print("Ya Benar")
	elif tebakan < angkaBenar:
		print(f"Angkanya lebih besar dari {tebakan}")
	elif tebakan > angkaBenar:
		print(f"Angkanya lebih kecil dari {tebakan} ")