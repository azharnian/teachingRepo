N1, N2, N3, N4 = map(float, input().split())

AVG = (2*N1+3*N2+4*N3+1*N4)/(2+3+4+1)

if AVG >=7:
	print(f"Media: {AVG:.1f}")
	print("Aluno aprovado.")
elif AVG >= 5:
	NR = float(input())
	print(f"Media: {AVG:.1f}")
	print("Aluno em exame.")
	print(f"Nota do exame: {NR:.1f}")
	print("Aluno aprovado.")
	print(f"Media final: {(AVG+NR)/2:.1f}")
else:
	print(f"Media: {AVG:.1f}")
	print("Aluno reprovado.")