# something = input().split(":") #delimiter
# print(something)
# a, b, c = something #
# print(a,b,c)

c1, n1, p1 = input().split()
c2, n2, p2 = input().split()
c1, n1, c2, n2, p1, p2  = int(c1), int(n1), int(c2), int(n2), float(p1), float(p2)

pay = (n1*p1) + (n2*p2)
print(f"VALOR A PAGAR: R$ {pay:.2f}")