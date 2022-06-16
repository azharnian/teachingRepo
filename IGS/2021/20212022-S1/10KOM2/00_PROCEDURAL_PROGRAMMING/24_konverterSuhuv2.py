import os

def cetak_pilihan():
	print("Pilihan Menu:")
	print("'cf' konversi dari Celcius-Farenheit")
	print("'cr'")
	print("'ck'")
	print("'fc' konversi dari Farenheit-Celcius")
	print("'fr'")
	print("'fk'")
	print("'rc'")
	print("'rf'")
	print("'rk'")
	print("'kc'")

	print("'q' untuk keluar dari program")

# C:R:F:K = 5:4:9(+- 32):5 (+- 273)

def celcius_ke_farenheit(suhu_c):
	return 9.0 / 5.0 * suhu_c + 32

def farenheit_ke_celcius(suhu_f):
	return (suhu_f - 32) * 5.0 / 9.0

def farenheit_ke_reamur(suhu_f):
	return (suhu_f - 32) * 4.0 / 9.0

def reamur_ke_kelvin(suhu_r):
	return 5.0/4.0 * suhu_r + 273

def reamur_ke_farenheit(suhu_r):
	return 9.0/4.0 * suhu_r + 32


error = False
pilihan = None
while not error:
	os.system("clear") #cls
	cetak_pilihan()
	pilihan = input("Pilihan : ")
	if pilihan == 'cf':
		main_c = float(input("Suhu Celcius-nya : "))
		result = celcius_ke_farenheit(main_c)
		print(f"Farenheit : {result}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'fc':
		main_f = float(input("Suhu Farenheit-nya : "))
		print(f"Celcius : {farenheit_ke_celcius(main_f)}")
		input("Tekan ENTER untuk kembali ke Menu")
	elif pilihan == 'q':
		error = True


print("Bye bye..")