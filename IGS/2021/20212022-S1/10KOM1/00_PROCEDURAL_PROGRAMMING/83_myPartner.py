name = input() #ANAS
my_number = 0

for character in name.upper():
	my_number += ord(character) #65+...+65+..

print(f"Inisial Jodoh Kamu adalah {chr(my_number%26+ord('A'))}")