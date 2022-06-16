#Nesting: A list of dictionaries

alien_0 = {'color':'green', 'points':0}
alien_1 = {'color':'yellow', 'points':50}
alien_2 = {'color':'pink', 'points':100}

aliens = [alien_0, alien_1, alien_2]

"""
aliens = [
	{'color':'green', 'points':0},
	{'color':'yellow', 'points':50},
	{'color':'pink', 'points':100}
]
"""
for alien in aliens:
	print(alien)
