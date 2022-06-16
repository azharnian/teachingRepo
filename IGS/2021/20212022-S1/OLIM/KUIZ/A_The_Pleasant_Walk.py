# https://vjudge.net/problem/Gym-103433M

N, K = map(int, input().split())
a = list(map(int, input().split()))

# best_counter = 0
# counter = 0
# for i in range(N):
# 	counter += 1
# 	if i < N and i != 0:
# 		if a[i] == a[i-1] and counter > best_counter:
# 			best_counter = counter
# 			counter = 0
# print(best_counter)

best_counter = -1
counter = 1

for i in range(N):
	if a[i] != a[i-1] and i != 0:
		counter += 1
	else:
		counter = 1

	if counter > best_counter:
		best_counter = counter

print(best_counter)