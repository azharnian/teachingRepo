from random import randint

play = True

correct = randint(0,10)

player = int(input("Masukkan Angka Yang Akan Ditebak : "))

while play:
	if correct > player:
		print(f"\nAngkanya lebih besar dari {player}")
		player = int(input("Masukkan Angka Yang Akan Ditebak : "))
	elif correct < player:
		print(f"\nAngkanya lebih kecil dari {player}")
		player = int(input("Masukkan Angka Yang Akan Ditebak : "))
	else:
		print(f"\nTebakan Benar!!")
		play = False

