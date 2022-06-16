# N1, N2, N3, N4 = input().split()
# N1, N2, N3, N4 = float(N1), float(N2), float(N3), float(N4)

# numbers = input().split()
# for i in range(len(numbers)):
# 	float(numbers[i])
# N1, N2, N3, N4 = numbers

N1, N2, N3, N4 = map(float, input().split())

AVG = (2*N1+3*N2+4*N3+1*N4)/10

if AVG >= 7:
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