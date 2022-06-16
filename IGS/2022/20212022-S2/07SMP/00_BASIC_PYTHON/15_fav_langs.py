
fav_langs = {
	'jen' : ['c', 'ruby'],
	'edbert' : ['typescript', 'python'],
	'sean' : ['haskel', 'lua'],
	'clarissa' : ['golang', 'php']
}

for name, langs in fav_langs.items():
	print(f"{name.title()}'s favorite languages are : ")
	for lang in langs:
		print(f"\t{lang.upper()}")