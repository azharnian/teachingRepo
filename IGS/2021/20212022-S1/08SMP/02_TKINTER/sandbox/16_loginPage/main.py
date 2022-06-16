from tkinter import Tk, Frame

from settings import Settings # from settings.py file import Settings Class
from login_page import LoginPage
from content_page import ContentPage

class Window(Tk):

	def __init__(self, MyApp, *args, **kwargs):
		super().__init__(*args, **kwargs) # to inherit properly from Tk
		self.app = MyApp
		self.settings = MyApp.settings
		self.title(self.settings.title)
		self.geometry(f"{self.settings.width}x{self.settings.height}")
		self.users = {
			"admin" : {"password" : "12345"},
			"superadmin" : {"password" : "12345"}
		}

		self.pages = {}

		self.container = Frame(self, bg="red")
		self.container.pack(fill="both",expand=True)

		self.container.grid_rowconfigure(0, weight=1)
		self.container.grid_columnconfigure(0, weight=1)
		self.pages["content_page"] = ContentPage(self.container, self)
		self.pages["login_page"] = LoginPage(self.container, self, bg="green")
		


class App:

	def __init__(self):
		self.settings = Settings()
		self.window = Window(self)

	def click_login_button(self):
		username = self.window.pages['login_page'].entry_username_var.get() # translate ui tkinter -> original string
		password = self.window.pages['login_page'].entry_password_var.get()
		#print(username, password)
		if username == "admin" and password == "12345":
			self.window.pages["content_page"].tkraise()
		else:
			print("login failed")
		self.window.pages['login_page'].entry_username.configure(textvariable="")
		self.window.pages['login_page'].entry_password.configure(textvariable="")

	def click_logout_button(self):
		self.window.pages["login_page"].tkraise()

	def run(self):

		self.window.mainloop()

my_app = App()
my_app.run()

