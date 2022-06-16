"""
C : F : R : K
5 : 9 (+- 32) : 4 : 5 (+- 273)
"""
import os
suhu_asal = None
suhu_tujuan = None
nilai_suhu_asal = 0
nilai_suhu_tujuan = 0

ratio_asal = 0
ratio_tujuan = 0

tambahan = 0
pengurangan = 0

play = True

while play: #infinite loop
	
	os.system('clear')
	print("\nMasukkan kode suhu asal : C (celcius) R (reamur) F (farenheit) K (kelvin)")
	suhu_asal = input("C/R/F/K: ").lower()
	nilai_suhu_asal = float(input("Nilai suhunya : "))

	print("\nMasukkan kode suhu tujuan : C (celcius) R (reamur) F (farenheit) K (kelvin)")
	suhu_tujuan = input("C/R/F/K: ").lower()

	pengurangan = 0
	tambahan = 0

	if suhu_asal == 'c':
		ratio_asal = 5
	elif suhu_asal == 'r':
		ratio_asal = 4
	elif suhu_asal == 'f':
		ratio_asal = 9
		pengurangan = 32
	elif suhu_asal == 'k':
		ratio_asal = 5
		pengurangan = 273

	if suhu_tujuan == 'c':
		ratio_tujuan = 5
	elif suhu_tujuan == 'r':
		ratio_tujuan = 4
	elif suhu_tujuan == 'f':
		ratio_tujuan = 9
		tambahan = 32
	elif suhu_tujuan == 'k':
		ratio_tujuan = 5
		tambahan = 273

	nilai_suhu_tujuan = (nilai_suhu_asal - pengurangan) * (ratio_tujuan/ratio_asal) + tambahan
	print(f"{nilai_suhu_asal} {suhu_asal} = {nilai_suhu_tujuan} {suhu_tujuan}")

	pilihan = input("Mau lanjut mengkonversi suhu ? (y/n) ").lower()

	if pilihan != "y":
		print("bye bye ...")
		play = False






