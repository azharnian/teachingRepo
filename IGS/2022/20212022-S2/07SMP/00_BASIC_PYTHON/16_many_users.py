
# users = {
# 	'aeinstein' : ['albert', 'einstein', 'princeton'],
# 	'mcurie' : ['marie', 'curie', 'paris']
# }


users = {
	'aeinstein' : {
		'first_name' : 'albert',
		'last_name' : 'einstein',
		'location' : 'princeton'
	},

	'mcurie' : {
		'first_name' : 'marie',
		'last_name' : 'curie',
		'location': 'paris'
	}
}


for username, user_info in users.items():
	print(f"\nUsername : {username}")
	fullname = f"{user_info['first_name']} {user_info['last_name']}"
	location = f"{user_info['location']}"

	print(f"\tFullname : {fullname.title()}")
	print(f"\tLocation : {location.title()}")