N = float(input())

if N == int(N):
	floor = int(N)
	ceil = int(N)
else:
	if N > 0:
		floor = int(N)
		ceil = int(N) + 1
	else :
		ceil = int(N)
		floor = int(N) - 1
print(floor, ceil)
"""
4.0
f = 4
c = 4

3.1
f = 3
c = 4

-3.1
f = -4
c = -3
"""