string = "syahrini"

list_chars = ["s","y","a","h","r","i","n","i"]

print(len(string))
print(len(list_chars))

for char in string:
	print(char, end=" ")
print()

for char in list_chars:
	print(char, end=" ")
print()

#slicing lists dan string
print(string[0], list_chars[0])
print(string[0:3], list_chars[0:3]) # start, stop
print(string[0:5:2], list_chars[0:5:2]) # start, stop, step