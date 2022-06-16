#sebuah kantin
#jam makan siang,
#kalau makan kurang dari/= jam 11 : salak
#kalau kita makan kurang dari/= jam 12 : semangka
#kalau makan kurang dari/= jam 13 : strawberry
#kalau kita makan lewat jam 13 : sirsak
# <= 11 : salak
# 11 - 12 : semangka
# > 12 : sirsak comment komentar

time = int(input("Jam Berapa : "))

#bottom to top
if time <= 11:
	print("Salak")
elif time <= 12:
	print("Semangka")
elif time <= 13:
	print("Strawberry")
else:
	print("Sirsak")
	

#top to bottom
if time > 13:
	print("Sirsak")
elif time > 12:
	print("Strawberry")
elif time > 11:
	print("Semangka")
else:
	print("Salak")
