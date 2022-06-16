N = int(input())

winner = None
for i in range(N):
	country = input().split()
	if i == 0:
		winner = country
	
	if int(country[0]) > int(winner[0]):
		winner = country
	elif int(country[0]) == int(winner[0]) and int(country[1]) > int(winner[1]):
		winner = country
	elif int(country[0]) == int(winner[0]) and int(country[1]) == int(winner[1]) and int(country[2]) > int(winner[2]):
		winner = country

for item in winner[3:]:
	print(item, end=" ")
print()
