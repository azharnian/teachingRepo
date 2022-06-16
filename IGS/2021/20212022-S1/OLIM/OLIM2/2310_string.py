kalimat, kata = input().split()
clear = False
while not clear:
	if kata not in kalimat:
		clear = True
	else:
		res = ""
		noted_index = []
		index = 0

		for char in kalimat:
			if kalimat[index:(index+len(kata))] == kata:
				for i in range(index,index+len(kata)):
					noted_index.append(i)
			index+=1

		for index in range(len(kalimat)):
			if index not in noted_index:
				res += kalimat[index]
		kalimat = res

print(res)