money = int(input())
banknotes = [100, 50, 20, 10, 5, 2, 1]

counter = 0
print(money)
while counter < len(banknotes):
	note = money // banknotes[counter]
	money = money % banknotes[counter]
	print(f"{note} nota(s) de R$ {banknotes[counter]},00")
	counter += 1