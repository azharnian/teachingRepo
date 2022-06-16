"""
1. Bayangkan kalian akan pergi ke 5 destinasi wisata
2. Buatkan lists dari 5 tempat tersebut dan tidak perlu terurut secara alphabet
3. Cetak lists yang original
4. Cetak lists terurut tanpa mengubah lists yg asli
5. Karena dana terbatas hapus 2 tujan, yg pertama hapus item di index 3, yg kedua hapus item index terakhir
6. Tiba-tiba ada sponsor yg mendanai pergi ke paris, masukkan kota paris sebagai tujuan pertama di lists.
7. Cetak lists setelah diurutkan permanen dan secara descending (Z-A)
Cl ini dikumpul di moodle menggunakan link pastebin.

"""
cities = ['bangkok', 'tokyo', 'new york', 'moskow', 'brazil'] #2
print(cities) #3
print(sorted(cities)) #4
cities.pop(3)
cities.pop(-1) #5
cities.insert(0, 'paris') #6
cities.sort(reverse=True)
print(cities) #7