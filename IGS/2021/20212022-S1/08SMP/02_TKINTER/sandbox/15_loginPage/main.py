from tkinter import Tk, Frame

from settings import Settings # from settings.py file import Settings Class
from login_page import LoginPage
from content_page import ContentPage


class Window(Tk):

	def __init__(self, MyApp, *args, **kwargs):
		super().__init__(*args, **kwargs) # to inherit properly from Tk
		self.settings = MyApp.settings
		self.title(self.settings.title)
		self.geometry(f"{self.settings.width}x{self.settings.height}")

		self.pages = {}

		self.container = Frame(self, bg="red")
		self.container.pack(fill="both",expand=True)

		self.container.grid_rowconfigure(0, weight=1)
		self.container.grid_columnconfigure(0, weight=1)
		self.pages["login_page"] = LoginPage(self.container, self, bg="green")
		#self.pages["content_page"] = ContentPage(self.container, self)



class App:

	def __init__(self):
		self.settings = Settings()
		self.window = Window(self)

	def run(self):

		self.window.mainloop()

my_app = App()
my_app.run()

