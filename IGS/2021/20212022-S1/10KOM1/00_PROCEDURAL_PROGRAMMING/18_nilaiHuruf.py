"""

Guru akan memberikan nilai huruf ke siswa
dengan aturan sebagai berikut
A >= 90
B >= 75
C >= 65
D >=50
F


"""

#top to bottom

nilai = float(input("Berapa nilainya: "))
if nilai >= 90:
	print("A")
elif nilai >= 75:
	print("B")
elif nilai >= 65:
	print("C")
elif nilai >= 50:
	print("D")
else:
	print("F")