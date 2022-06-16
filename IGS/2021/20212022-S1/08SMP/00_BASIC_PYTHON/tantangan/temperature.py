#Program ini untuk mengkonversi suhu dari (C/F/R) ke (C/F/R)
# C:F:R = 5:9:4 ->
# Ke Farenheit +32(setelah dikali), Dari Farenheit -32(sebelum dikali)

#Tambahin Suhu Kelvin -> 5 (-273) / (+273)

userRespond = None

initScale = None
initValue = 0

finalScale = None
finalValue = 0

knownScale = 0
askedScale = 0

add = 0
subtract = 0

#Flag Looping
running = True

while running:
	
	print("\nChoose Init Scale Temperature : Celcius(C)/Reamur(R)/Farenheit(F)")
	initScale = input("C/R/F : ").lower()
	initValue = float(input("Input Value in Degrees : "))

	print("\nChhoose Final Scale Temperature : Celcius(C)/Reamur(R)/Farenheit(F)")
	finalScale = input("C/R/F : ").lower()

	add = 0
	subtract = 0

	if initScale == "c":
		knownScale = 5
	elif initScale == "r":
		knownScale = 4
	elif initScale == "f":
		knownScale = 9
		subtract = 32
	else:
		knownScale = 1

	if finalScale == "c":
		askedScale = 5
	elif finalScale == "r":
		askedScale = 4
	elif finalScale == "f":
		askedScale = 9
		add = 32
	else:
		askedScale = 1


	finalValue = ((initValue - subtract) * (askedScale/knownScale)) + add

	print(f"\n{initValue:.1f}{initScale} = {finalValue:.1f}{finalScale}")

	userRespond = input("Do you want to continue ? (Y/N) : ").lower()

	if userRespond == "n":
		running = False



