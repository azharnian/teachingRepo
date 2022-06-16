# a, b, c = input().split()
# a, b, c = int(a), int(b), int(c)

#map ...

numbers = input().split()
for i in range(len(numbers)):
	int(numbers[i])

numbers = map(int, input().split())