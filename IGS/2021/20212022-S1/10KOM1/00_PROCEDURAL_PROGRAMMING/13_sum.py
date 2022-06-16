a = 1 #tempat user input data
s = 0 #tempat angka hasil jumlah
while a != "q":
	print("Current Sum:", s)
	a = float(input('Number ? '))
	s = s + a

print("Total Sum =", s)