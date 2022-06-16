from tkinter import Tk, Frame

from settings import Settings # from settings.py file import Settings Class


class Window(Tk):

	def __init__(self, MyApp):
		super().__init__()
		self.settings = MyApp.settings
		self.title(self.settings.title)
		self.geometry(f"{self.settings.width}x{self.settings.height}")

		self.pages = {}

		self.container = Frame(self, bg="grey")
		self.container.pack(fill="both",expand=True)

class App:

	def __init__(self):
		self.settings = Settings()
		self.window = Window(self)
		#self.window.title("My First App")

	def run(self):

		self.window.mainloop()

my_app = App()
my_app.run()


"""
window = Tk()
window.title("My First App")
window.mainloop()
"""