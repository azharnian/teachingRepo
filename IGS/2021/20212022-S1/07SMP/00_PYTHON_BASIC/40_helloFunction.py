
def hello_to_you():
	print("Hello ... how do you do !")
	print("Thank you very much ...\n")

def hello_to(condition, person): #argumen function
	print(f"Good {condition}")
	print(f"Hello {person} how do you do !")
	print(f"Thank you very much {person}\n")


counter = 0
while counter < 3:
	hello_to("Morning","Dylan")
	counter += 1