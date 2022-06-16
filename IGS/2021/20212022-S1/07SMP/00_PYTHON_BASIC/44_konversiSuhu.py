
def munculin_menu():
	print("Pilihan : ")
	print("""
		cf : konversi dari Celcius Ke Farenheit
		fc : konversi dari Farenheit Ke Celcius
		rc :
		rf :
		cr :
		q : keluar program
	""")

def ubah_celcius_jadi_farenheit(suhu):
	hasil = 9.0/5.0 * suhu + 32
	print(f"Farenheit : {hasil}")

def ubah_farenheit_jadi_celcius(suhu):
	hasil = (suhu_farenheit - 32) * 5.0 / 9.0
	print(f"Celcius : {hasil}")

pilihan = None #flag..

while pilihan != "q":
	munculin_menu()
	pilihan = input("Masukkan pilihan Anda : ")
	if pilihan == "cf":
		suhu_celcius = float(input("Suhu Celciusnya : "))
		ubah_celcius_jadi_farenheit(suhu_celcius)

	elif pilihan == "fc":
		suhu_farenheit = float(input("Suhu Farenheitnya : "))
		ubah_farenheit_jadi_celcius(suhu_farenheit)