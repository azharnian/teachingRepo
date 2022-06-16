
filename = input("Filename is = ")  #'alice.txt'

"""
2^0 = 1, 2^1 = 2 .... 2^8 = 256, 0-255
"""
try:
	with open(filename, 'r', encoding='utf-8') as data:
		contents = data.read()
except FileNotFoundError as e:
	print(f"Sorry, The file does not exist.\n{e}")
else:
	length = len(contents)
	print(f"The file {filename} has about {length} words.")

#"Sorry the file does not exists."

