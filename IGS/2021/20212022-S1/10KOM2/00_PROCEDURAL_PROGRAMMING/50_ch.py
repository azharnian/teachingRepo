"""
1. Buat 3 dictionary yg menampilkan orang yg berbeda (ob: person), dan simpan ketiganya di dalam sebuah list (ls: people). Untuk key dan value (informasi masing-masing orang harus seragam (key sama), val beda, banyak key minimal 3. Loop semua ls dari people dan tampilkan setiap informasi dari masing-masing orang dengan cara kalian sendiri.

2. Buat 4 Hewan Peliharaan dengan menggunakan dictionary. Disetiap hewan peliharaan setidaknya memiliki informasi mengenai jenis hewan (typeOfPet), nama pemilik (ownersname), dan ditambah 2 infolain sesuai keinginan kalian. Simpan 4 hewan peliharaan tsb ke dalam lists, kemudian tampilkan masing2 informasi hewan peliharaan menggunakan looping apapun.

3. Buat dictionary dengan nama cities. Gunakan nama kota sebagai key di dalam dict tsb. Kemudian buatkan dictionary untuk setiap kota (minimal 2), agar dapat menyimpan informasi seperti, populasi dan fun fact. Dan tampilkan setiap kota beserta info2nya dengan menggunakan looping.

"""

#1
"""
people = [
	{'name':'ali', 'hobby':'cooking', 'phone':'234'},
	{'name':'bobby', 'hobby':'free fire', 'phone':'123'},
	{'name':'cindy', 'hobby':'barbie', 'phone':'567'}
]

for person in people:

	for key, val in person.items():
		print(f"{key} \t: {val}")

	print()
"""
#2