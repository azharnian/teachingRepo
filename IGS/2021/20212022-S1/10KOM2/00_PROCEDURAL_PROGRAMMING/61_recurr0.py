
#print angka 1 - 10, menggunakan recursion

def oneToTen(init, final):
	print(init, end=" ")
	if init < final:
		return oneToTen(init+1, final)
	print()

def oneToTenWhile(init, final):
	while init <= final:
		print(init, end=" ")
		init += 1
	print()

oneToTen(1, 10)
oneToTenWhile(1, 10)