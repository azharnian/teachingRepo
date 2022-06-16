fav_lang = {
	'Vito' : 'Pascal',
	'Dylan' : 'Python',
	'Edbert' : 'Golang',
	'Daniel' : 'Swift'
}

phone_books = {
	'Justin' : '081122334455',
	'Aneira' : '080910002000',
	'Dzaki' : '081930306060',
	'Anas' : '0899887766'
}

print(f"Anas' phone number is {phone_books['Anas']}.")

#access value using get() / searching in dict

print(phone_books.get('Dzaki'))
print(phone_books.get('Michelle'))
print(phone_books.get('Obama', 'No Mr Obama'))