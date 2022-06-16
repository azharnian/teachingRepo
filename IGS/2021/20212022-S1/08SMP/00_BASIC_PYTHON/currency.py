
userRespond = None

initCurrency = None
initValue = 0

finalCurrency = None
finalValue = 0

knownRatioInitCurrency = 0
askedRatioFinalCurrency = 0

error = False

currency_data = {
	'BTC' : 1,
	'USD' : 39753,
	'DGC' : 102864,
	'KRW' : 44874771,
	'IDR' : 574580949
}

while not error:
	print("\nChoose Init Currency : BTC/USD/DGC/KRW/IDR")
	initCurrency = input("==> : ").upper()
	initValue = float(input("Input how much do you have : "))

	print("\nChhoose Final Currency : BTC/USD/DGC/KRW/IDR")
	finalCurrency = input("==> : ").upper()

	if initCurrency in currency_data:
		knownRatioInitCurrency = currency_data[initCurrency]
	else:
		knownRatioInitCurrency = 1

	if finalCurrency in currency_data:
		askedRatioFinalCurrency = currency_data[finalCurrency]
	else:
		askedRatioFinalCurrency = 1

	finalValue = initValue * (askedRatioFinalCurrency/knownRatioInitCurrency)
	print(f"\n{initValue:.1f}{initCurrency} = {finalValue:.1f}{finalCurrency}")

	userRespond = input("Do you want to continue ? (Y/N) : ").lower()

	if userRespond == "n":
		error = True


