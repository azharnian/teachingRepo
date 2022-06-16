code1, amount1, price1 = input().split(" ")
code1, amount1, price1 = int(code1), int(amount1), float(price1)

code2, amount2, price2 = input().split(" ")
code2, amount2, price2 = int(code2), int(amount2), float(price2)

total = (amount1*price1) + (amount2*price2)

print(f"VALOR A PAGAR: R$ {total:.2f}")