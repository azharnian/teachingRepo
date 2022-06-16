"""
from hitungan.mtk import phi
"""
from . import mtk

gravitasi = 9.8

def tekanan_tiang(m, x, y):
	return (m*gravitasi)/(x*y)

def tekanan_pipa(m, r):
	# return (m*gravitasi)/(phi*r**2)
	return (m*gravitasi)/(mtk.phi*r**2)