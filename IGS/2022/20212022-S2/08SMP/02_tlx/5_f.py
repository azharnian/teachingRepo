N = float(input())

if N == int(N):
	print(int(N), int(N))
else:
	if N > 0:
		floor = int(N)
		ceil = floor +1
	else:
		ceil = int(N)
		floor = ceil - 1

	print(floor, ceil)