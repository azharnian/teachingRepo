#23_aliens.py > nesting : a list of dictionaries

alien_0 = {"color":"green", "points":20}
alien_1 = {"color":"red", "points":0}
alien_2 = {"color":"purple", "points":100}

aliens = [alien_0, alien_1, alien_2]

"""
aliens = [
	{"color":"green", "points":20},
	{"color":"red", "points":0},
	{"color":"purple", "points":100}
]
"""
for alien in aliens:
	print(f"Alien {aliens.index(alien)}")
	for key, value in alien.items():
		print(f"{key.title()} : {str(value).upper()}")

	print()