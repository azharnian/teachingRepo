import os
import time

def cetak_pilihan():
	print("Pilihan : ")
	print("cf - konversi dari Celcius ke Farenheit")
	print("cr - ")
	print("ck - ")

	print("fc - konversi dari Farenheit ke Celcius")
	
	print("q - keluar dari program")

# C:R:F:K = 5:4:9(+- 32):5(+- 273)

def celcius_ke_farenheit(suhu_c):
	return 9.0 / 5.0 * suhu_c + 32

def farenheit_ke_celcius(suhu_f):
	return (suhu_f - 32) * 5.0 / 9.0

running = True
pilihan = None
while running:
	os.system("clear") #cls untuk windows
	cetak_pilihan()
	pilihan = input("Pilihan : ")

	if pilihan == "cf":
		main_c = float(input("Suhu Celcius-nya : "))
		result = celcius_ke_farenheit(main_c)
		print(f"Farenheit : {result}")

		input("Tekan ENTER untuk ke MENU UTAMA")
	elif pilihan == "fc":
		main_f = float(input("Suhu Farenheit-nya : "))
		print(f"Celcius : {farenheit_ke_celcius(main_f)}")

		input("Tekan ENTER untuk ke MENU UTAMA")
	elif pilihan == "q":
		running = False
		print("Bye bye, [Keluar dalam 1 detik]")
		time.sleep(1)