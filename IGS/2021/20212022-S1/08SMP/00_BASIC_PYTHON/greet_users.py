def greet_users(names):
	for name in names:
		msg = f"Hello, {name.title()}"	
		print(msg)

users = ['hanna', 'bobby', 'andi']
greet_users(users)

list_a = []

list_b = list_a[:]

list_c = list_a