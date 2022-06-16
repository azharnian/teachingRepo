#argument dan return

def luas_persegi(sisi):
	return sisi * sisi

def luas_segitiga(alas, tinggi):
	return (alas * tinggi)/2

def luas_trapesium(sisi_a, sisi_b, tinggi):
	return (sisi_a+sisi_b)*tinggi/2

def luas_lingkaran(jari):
	if jari % 7 == 0:
		return 22*(jari**2/7)
	else:
		return 3.14159 * jari**2

print(luas_persegi(20)) #ada angka di sini.
print(luas_segitiga(10, 20))
print(luas_lingkaran(14))