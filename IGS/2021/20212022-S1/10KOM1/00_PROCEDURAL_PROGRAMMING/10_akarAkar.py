#import math
# X^2 + 5X + 6 -> X1 = -3 atau X2 = -2
from math import sqrt

a = float(input("Koef X^2 : "))
b = float(input("Koef X : "))
c = float(input("Konstanta : "))
D = b**2 - (4*a*c)
x1 = (-b + sqrt(D)) / (2 * a)
x2 = (-b - sqrt(D)) / (2 * a)
print("Akar X1 =", x1)
print("Akar X2 =", x2)