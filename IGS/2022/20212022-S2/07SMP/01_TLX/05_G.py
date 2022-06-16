x1, y1, x2, y2 = input().split(" ")
x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

selisihX = x1-x2
if selisihX < 0:
	selisihX = -selisihX

selisihY = y1-y2
if selisihY < 0:
	selisihY = -selisihY

hasil = selisihX + selisihY
print(hasil)