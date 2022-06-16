a = 0
b = 1
count = 0
max_count = 20


while count < max_count:
	count += 1 # increasing var
	print(a, end=" ")

	old_a = a
	a = b
	b = old_a + a

print()