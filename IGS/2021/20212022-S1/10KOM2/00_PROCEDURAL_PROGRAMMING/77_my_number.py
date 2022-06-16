name = input() # ANAS
#Pakai For Loop
my_number = 0
for char in name.upper():
	my_number += ord(char)
#print(my_number) # 65+79+65+84 65-97
print("Inisial Jodoh Kamu : ", chr(my_number%26 + ord("A"))) #J