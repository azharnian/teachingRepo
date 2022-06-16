N = int(input())

if N < 10:
	print("satuan")
elif N < 100:
	print("puluhan")
elif N < 1000:
	print("ratusan")
elif N < 10000:
	print("ribuan")
else:
	print("puluhribuan")
