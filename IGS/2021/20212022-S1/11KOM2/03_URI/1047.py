iH, iM, fH, fM = input().split()
iH, iM, fH, fM = int(iH), int(iM), int(fH), int(fM)

hours = fH-iH

minutes = fM-iM

if hours <= 0 and fM <= iM:
	hours += 24

if minutes < 0:
	hours -= 1
	minutes += 60

print(f"O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)")