
favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'alex' : 'lua',
	'mike' : 'python'
}
#lists, dict, dict_keys, dict_values, tuple, set
# print(list(favorite_languages.keys()))
# print(tuple(favorite_languages.values()))

rgb_color = (255, 255, 255) #rgb
position = (100, 200) # xy
screen_size = (1280, 860)


#for name, lang in favorite_languages.items():
	# print(f"{name.title()}'s favorite language is {lang.title()}.")

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

print("The following languages have been mentioned: ")
for lang in sorted(set(favorite_languages.values())):
	print(lang)

