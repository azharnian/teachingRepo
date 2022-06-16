from sys import argv, exit

# for arg in argv:
# 	print(arg)

if len(argv) <= 2:
	print("Missing command line argument, please check docs.")
	exit(1)

print(argv)
exit(0)