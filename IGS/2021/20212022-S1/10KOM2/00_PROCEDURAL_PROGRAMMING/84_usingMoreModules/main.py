# 180 deg = pi rad
from math import sin, pi, radians
from random import randint
from datetime import datetime as dt

def sin_versi_saya(angle):
	return sin(radians(angle))

def lempar_dadu():
	return randint(1,6)
"""
print(sin(pi/6)) #0.5 radians (rad) / degrees (derajat)
print(sin(radians(30)))
print(sin_versi_saya(30))
"""

print(lempar_dadu())
print(dt.now()) #buka dokumentasi
print(dt.now().year)
