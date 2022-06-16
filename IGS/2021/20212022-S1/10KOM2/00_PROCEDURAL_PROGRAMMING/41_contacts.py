
#json - > javascript object notation
fav_lang = {
	'Adri' : 'C',
	'Alfons' : 'Swift',
	'Chelvi' : 'GoLang'
}

contacts = {
	'Jesse' : '0817335421',
	'Justin' : '089965432112',
	'Rayvin' : '081323454321',
	'Anas' : '0813432156789'
}

print(f"Anas' number phone is {contacts['Anas']}.")

#access value using get() / searching in dictionary

rayvin = contacts.get('Rayvin')
print(rayvin)
mr_x = contacts.get('mr x')
print(mr_x)
mr_y = contacts.get('mr y', 'no mr y')
print(mr_y)