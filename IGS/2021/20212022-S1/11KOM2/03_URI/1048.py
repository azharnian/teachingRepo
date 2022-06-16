salary = float(input())

if salary > 2000:
	percent = 4
elif salary > 1200:
	percent = 7
elif salary > 800:
	percent = 10
elif salary > 400:
	percent = 12
else:
	percent = 15

new_sal = salary + (salary * (percent/100))
earned = new_sal - salary
val_percent = (earned / salary) * 100

print(f"Novo salario: {new_sal:.2f}")
print(f"Reajuste ganho: {earned:.2f}")
print(f"Em percentual: {val_percent:.0f} %")