

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

Mab = (a + b + abs(a - b))/2

Mf = (Mab + c + abs(Mab - c))/2

print(f"{int(Mf)} eh o maior")