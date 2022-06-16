from hitungan.mat.matematika import luas_persegi, luas_lingkaran
gravitasi = 9.8

def tekanan_tiang(m, x, y):
	return m*gravitasi/luas_persegi(x,y)

def tekanan_pipa(m, r):
	return m*gravitasi/luas_lingkaran(r)