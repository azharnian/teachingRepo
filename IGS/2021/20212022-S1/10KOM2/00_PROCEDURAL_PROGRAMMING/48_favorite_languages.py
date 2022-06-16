
favorite_languages = {
	'jen' : ['python', 'javascript'],
	'sarah' : ['c'],
	'edward' : ['go', 'typescript'],
	'bill' : ['haskel', 'python']
}

for name, languages in favorite_languages.items():
	print(f"{name.title()}'s favorite languages are:")

	for language in languages:
		print(f"\t{language.upper()}")