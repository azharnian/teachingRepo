from os import system as s

def print_menu():
	print('1. Print Phone Numbers')
	print('2. Add a Phone Numbers')
	print('3. Remove a Phone Numbers')
	print('4. Search a Phone Numbers')
	print('5. Quit')

def menu_1_print_phone_numbers():
	s('clear') # cls for windows
	if len(phones) > 0:
		print('Contact List\n')
		header = "NAME\tPHONE"
		break_line = "-*-*-\t-*-*-"
		print(header+"\n"+break_line+"\n")
		for name,nphone in phones.items():
			print(f'{name}\t{nphone}')
	else:
		print('There is no contact yet.')
	input('Enter To Back ...')

def menu_2_add_phone_numbers():
	s('clear') #cls for windows
	print('Add New Contact')
	name = input('\nName\t:')
	nphone = input('Phone\t:')
	confirm = input(f'\nAre you sure to save {name.title()} - {nphone} ? (y/n) ')
	if confirm.lower() == 'y':
		phones[name] = nphone
		print('Contact added.')
	else:
		print('Add new contact canceled.')
	input('Enter To Back ...')

def check_user_input(user_input):
	if user_input == '5':
		return True
	elif user_input == '1':
		menu_1_print_phone_numbers()
		return False
	elif user_input == '2':
		menu_2_add_phone_numbers()
		return False
	else:
		return False

stop = False #flag for stop looping
user_input = None
phones = {}

while not stop:
	s('clear') #clear screen
	print_menu() #print menu apps
	prompt = 'Enter Your Choice :' #set prompt from computer
	user_input = input(prompt) #request user input for menu
	stop = check_user_input(user_input) #check user input
	