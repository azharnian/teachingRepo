import os
def print_menus():
	print("""\n
	** ELEMENTS ENCYCLOPEDIA ***
	[1] List of Elements
	[2] Add new element
	[3] Edit element
	[4] Delete element
	[5] Find element
	[Q] Quit Program
	""")

def print_elements():
	#.. put your code here
	input("Press ENTER to return.")

elements = { #key -> element symbol, #val -> info
	"Na" : {
		"names" : "Natrium",
		"object" : "Salt",
		"fun fact" : []
	},
	"Ca" : {
		"names" : "Calcium",
		"object" : "Milk",
		"fun fact" : []
	}
}

running = True
while running:
	os.system("clear") #windows : cls
	print_menus()
	option = input("Put your option : ")
	if option.lower() == "q":
		running = False
	elif option == "1":
		print_elements()


print("Thanks ...")