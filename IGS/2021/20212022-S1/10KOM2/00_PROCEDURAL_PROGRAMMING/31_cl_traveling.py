"""
1. Bayangkan kita akan pergi ke 5 tempat baru
2. Buatkan lists dari 5 tempat tersebut dan tidak perlu terurut
3. Cetak lists yg original
4. Cetak lists terurut tanpa mengubah list yg asli
5. Karena dana terbatas hapus 2 tujuan, yang pertama hapus item di index 3, yang kedua hapus item index terakhir.

6. Tiba-tiba ada sponsor yg mendanai pergi ke paris, masukkan kota paris sebagai tujuan pertama di list.
7. cetak list setelah diurutkan permanen dan secara descending (Z-A)
dikumpul di moodle gunakan link pastebin.
"""
jalanJalan = ['Pantai Kuta', 'Bandung', 'New York', 'Mekkah'] #2
print(jalanJalan) #3
print(sorted(jalanJalan)) #4
jalanJalan.pop(3)
jalanJalan.pop(-1)#5
jalanJalan.insert(0, 'Paris')#6
jalanJalan.sort(reverse=True)
print(jalanJalan)