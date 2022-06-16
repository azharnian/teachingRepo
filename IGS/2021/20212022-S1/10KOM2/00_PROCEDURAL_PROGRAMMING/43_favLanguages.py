favorite_languages = {

	'jen' : 'python',
	'sarah' : 'c++',
	'edward' : 'ruby', #ruby on rails
	'alex' : 'lua',
	'mike' : 'python'
}

# lists, dict, tuple, dict_keys, dict_values, set : array
rgb_color = (100, 200, 0) # r,g,b
position = (30, 100) #x,y

print(favorite_languages.items()) # [(1, a), (2, b), ()]

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll")

my_list = ['a', 'b', 'c', 'a']
print(set(my_list))

print(sorted(set(favorite_languages.values())))

for language in sorted(set(favorite_languages.values())):
	print(f"{language}")