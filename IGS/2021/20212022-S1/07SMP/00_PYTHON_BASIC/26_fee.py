"""
Indri ingin berjualan di sebuah lapangan. Akan tetapi
ada seorang preman bernama Gosh. Gosh memberitahu
jika indri ingin berjualan di lapangan tersebut, maka
harus membayar sejumlah uang dengan peraturan sebagai 
berikut.

100_000 : 4 m_persegi
500_000 : 10 m_persegi
1_000_000 : 18 m_persegi
2_000_000 : 28 m_persegi

Indri memiliki uang sebesar 1_200_000
"""
# kecil -> besar
uangIndri = int(input("Berapa uang Indri : "))
# if uangIndri < 100_000:
# 	print("Tidak mendapatkan lapak.")
# elif uangIndri < 500_000:
# 	print("Dapat lapak 4 m persegi.")
# elif uangIndri < 1_000_000:
# 	print("Dapat lapak 10 m persegi.")
# elif uangIndri < 2_000_000:
# 	print("Dapat lapak 18 m persegi.")
# else:
# 	print("Dapat lapak 28 m persegi.")

# besar  -> kecil
if uangIndri >= 2_000_000:
	print("Dapat lapak 28 m persegi.")
elif uangIndri >= 1_000_000:
	print("Dapat lapak 18 m persegi.")
elif uangIndri >= 500_000:
	print("Dapat lapak 10 m persegi.")
elif uangIndri >= 100_000:
	print("Dapat lapak 4 m persegi.")
else:
	print("Tidak mendapatkan lapak.")






