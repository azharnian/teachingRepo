
A, B, C = input().split()
A, B, C = float(A), float(B), float(C)

seg = (A*C)/2
ling = 3.14159 * C**2
tra = (A+B) * C /2
per = B**2
ppan = A*B

print(
f"""TRIANGULO: {seg:.3f}
CIRCULO: {ling:.3f}
TRAPEZIO: {tra:.3f}
QUADRADO: {per:.3f}
RETANGULO: {ppan:.3f}""")