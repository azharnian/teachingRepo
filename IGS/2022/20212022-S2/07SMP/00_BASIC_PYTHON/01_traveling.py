"""
Gunakan Lists
1. Bayangkan kita akan pergi ke 5 tempat baru, buatkan lists dari 5 tempat tersebut dan tidak perlu terurut.
2. Cetak lists original nya. -> print
3. Karena dana terbatas hapus 2 tujuan. Yang pertama hapus item di index 3, yg kedua hapus item index terakhir.
4. Tiba-tiba ada donatur yg mendanai pergi ke paris. Masukkan kota paris sebagai tujuan pertama di list.
5. Cetak lists yang telah terurut sesuai abjad.

"""
#1
my_dreams = ["bali", "thailand", "new york", "tokyo", "arab"]
#2
print(my_dreams)

#3
my_dreams.pop(3)
my_dreams.pop(-1)

#4
my_dreams.insert(0, "paris")

#5
my_dreams.sort()
print(my_dreams)

