#import random
from random import randint
import os

os.system("clear") # clear
angkaBenar = randint(0, 10) #0-10
angkaTebakan = None

while angkaTebakan != angkaBenar:
	angkaTebakan = int(input("Angka Tebakannya = "))

	if angkaTebakan == angkaBenar:
		print("Yeay Anda benar!!")
	elif angkaTebakan > angkaBenar:
		print(f"Angkanya lebih kecil dari {angkaTebakan}")
	elif angkaTebakan < angkaBenar:
		print(f"Angkanya lebih besar dari {angkaTebakan}")
