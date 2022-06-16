#nesting dictionary in dictionary

users = { #key : username, value : data user {}
	'aeinstein' : {
		'first' : "albert",
		'last' : "einstein",
		'location' : "princeton"
	},
	'mcurie' : {
		'first' : "marie",
		'last' : "curie",
		'location' : "paris"
	}
	
}

for username, user_info in users.items():
	print(f"\nUsername : {username}")
	fullname = f"{user_info['first'].title()} {user_info['last'].title()}"
	location = user_info['location'].title()
	print(f"\tFullname:{fullname}")
	print(f"\tLocation:{location}")