
#empty list for storing aliens
aliens = []

#30 green aliens
for i in range(30):
	alien = {'color':'green', 'points':0}
	aliens.append(alien)

#show the first 5 aliens
for alien in aliens[0:5]: #aliens[:5] .5
	print(alien)

#how many aliens have been created
print(f"Total number of aliens is {len(aliens)}")