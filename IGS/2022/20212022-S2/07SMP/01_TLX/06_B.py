jumlah_kandang = int(input())
isi_kandang = input().split()

total_bebek = 0
for i in range(jumlah_kandang):
	total_bebek += int(isi_kandang[i])

print(total_bebek)