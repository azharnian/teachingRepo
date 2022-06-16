"""
in: -3
out: 3

in: 5
out: 5

"""
def jadiin_positif(number): # function -> def 
	if number < 0:
		print(number*-1)
	else:
		print(number)


input_number = int(input("Angkanya : "))
jadiin_positif(input_number)
