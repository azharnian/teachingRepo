from math import sqrt

x1, y1 = input().split()
x2, y2 = input().split()

distance = sqrt( (float(x1)-float(x2))**2  + ((float(y1)-float(y2))**2 ))

print(distance)