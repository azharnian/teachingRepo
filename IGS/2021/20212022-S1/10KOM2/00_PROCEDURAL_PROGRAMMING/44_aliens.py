#Nesting : A list of dictionaries
alien_0 = {'color':'green', 'points':10}
alien_1 = {'color': 'yellow', 'points':15}
alien_2 = {'color':'pink', 'points':20}

aliens = [alien_0, alien_1, alien_2]

"""
aliens = [
	{'color':'green', 'points':10},
	{'color': 'yellow', 'points':15},
	{'color':'pink', 'points':20}
]
"""
for alien in aliens:
	print(alien)