#dictionary ->  store data in to model a variety of real-world object accurately.

alien = {'color': 'green', 'skill':'jumping'} # real-world object model

#accessing
print(alien['color']) #key-value 
print(alien['skill'])


#adding more information
alien['pos_x'] = 30
alien['pos_y'] = 100
print(alien)

#Start with Empty Dictionary
player = {}
player['username'] = "budi445"
player['points'] = 50
player['skill'] = 'run'

#Modifying
player['username'] = "budi999"
player['points'] += 50

del player['skill']

houses = ["budi", "cindy", "denny"]

fav_lang = { # data storage
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'javascript'
}

contacts = {
	'anas' : '089933445566',
	'budi' : '081123456789'
}

print(f"The player {player['username']} has {player['points']} point(s).")