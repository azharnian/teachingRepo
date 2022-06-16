a = 0
b = 1
counter = 0
max_counter = 20

while counter < max_counter:

	counter += 1
	print(a, end=" ")
	b += a
	a = b - a

print()
