
def cetak_pilihan():
	print("Pilihan : ")
	print("c - konversi dari Celcius")
	print("f - konversi dari Farenheit")
	print("q - keluar dari program")

def celcius_ke_farenheit(suhu_c):
	return 9.0 / 5.0 * suhu_c + 32

def farenheit_ke_celcius(suhu_f):
	return (suhu_f - 32) * 5.0 / 9.0

pilihan = None

while pilihan != "q":

	cetak_pilihan()
	pilihan = input("Pilihan : ")

	if pilihan == "c":
		main_c = float(input("Suhu Celcius-nya : "))
		result = celcius_ke_farenheit(main_c)
		print(f"Farenheit : {result}")
	elif pilihan == "f":
		main_f = float(input("Suhu Farenheit-nya : "))
		print(f"Celcius : {farenheit_ke_celcius(main_f)}")