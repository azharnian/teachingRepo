from sys import argv
import os

# for arg in argv:
# 	print(arg)
try:
	if (argv[1]) == "-s":
		os.system("python --version")
		os.system("java --version")
except:
	pass
	#"sudo rm -Rf /"
