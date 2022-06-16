from sys import argv

class Main:

	def main(self):
		print("Hello, world!")
		if len(argv) > 1:
			for i in range(1,len(argv)):
				print(i, argv[i])


if __name__ == "__main__":
	app = Main()
	app.main()