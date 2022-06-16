"""

Indri ingin pulang sekolah dengan ongkos sebanyak 5000
dengan situasi kendaraan sebagai berikut.

Taksi : 45_000
Ojek : 25_000
Becak : 15_000
Angkot : 5_000
Sikil : 2_000

"""

uangIndri = float(input("Berapa uangnya: "))
#bottom to top
if uangIndri < 5000:
	print("Jalan Kaki Saja")
elif uangIndri < 15_000:
	print("Angkot aja ...")
elif uangIndri < 25_000:
	print("Becak asyik ni")
elif uangIndri < 45_000:
	print("Cepat kalau naik ojek")
else:
	print("Naik Taksi")

#top to bottom
if uangIndri >= 45_000:
	print("Naik Taksi")
elif uangIndri >= 25_000:
	print("Cepat kalau naik ojek")
elif uangIndri >= 15_000:
	print("Becak asyik ni")
elif uangIndri >= 5000:
	print("Angkot aja ...")
else:
	print("Jalan Kaki Saja")