money = float(input())
banknotes = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

money = money * 100
for banknote in banknotes:
	if banknote == 100:
		print("NOTAS:")
	elif banknote == 1:
		print("MOEDAS:")
	note = int(money // (banknote*100))
	money = money % (banknote*100)

	if banknote >= 2:
		print(f"{note} nota(s) de R$ {banknote:.2f}")
	else:
		print(f"{note} moeda(s) de R$ {banknote:.2f}")