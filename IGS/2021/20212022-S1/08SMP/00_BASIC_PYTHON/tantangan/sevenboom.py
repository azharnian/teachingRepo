# 1. cetak angka dari 1 s.d. 100 agar tiap
# angka kelipatan 7 di ganti dengan tulisan 'boom'

# clue:

# for number in range(1,101):
# 	if  kalau sisa bagi = 0 saat dibagi 7
# 	gunakan operator mod (%)

# (+) pakai function (def ...)

# input >
# intial_number :5 (int(input(...)))
# final_number :10

# output >
# 5
# 6
# boom
# 8
# 9
# 10

# angka di buat menjadi memiliki step 2 dari mulainya.
# output >
# 5
# boom
# 9
# 11
# 13
# 15
# 17
# 19
# boom

init_number = int(input('initial number : '))
final_number = int(input('final number : '))
# number += 1

for number in range(init_number,final_number+1,2):
	if number % 7 == 0 :
		print('boom')
	else:
		print(number)
