from sys import argv, exit

# for arg in argv:
# 	print(arg)

if len(argv) <= 2:
	print("Missing command line argument, please check documentation.")
	exit(1) # failed

print(argv)
exit(0) # success