from tkinter import Tk, Frame

import json

from settings import Settings
from login_page import LoginPage
from content_page import ContentPage

class Window(Tk):

	def __init__(self, Myapp, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.app = Myapp
		self.settings = Myapp.settings
		self.title(self.settings.title)
		self.geometry(f"{self.settings.width}x{self.settings.height}")

		self.pages = {}

		self.container = Frame(self, bg="red")
		self.container.pack(fill="both", expand=True)

		self.container.grid_rowconfigure(0, weight=1)
		self.container.grid_columnconfigure(0, weight=1)
		self.pages["content_page"] = ContentPage(self.container, self)
		# self.pages["login_page"] = LoginPage(self.container, self, bg="green")


class App:

	def __init__(self):
		self.settings = Settings()
		self.users = self.get_stored_json(filename="users.json")#self.get_stored_users()
		self.data = self.get_stored_json(filename="data.json")#self.get_stored_data()
		self.window = Window(self)

	def get_stored_json(self, filename):
		try:
			with open(filename, "r") as data: # Mode Read -> Read The File
				return json.load(data)
		except:
			return "doesn't exist .."


	def run(self):
		self.window.mainloop()

	def click_login_button(self):
		username = self.window.pages['login_page'].entry_username_var.get()  # transalte ui tkinter -> original string
		password = self.window.pages['login_page'].entry_password_var.get()
		# print(username, password)

		if username in self.users:
			if self.users[username]['password'] == password:
				# print("granted")
				self.window.pages["login_page"].label_error.configure(text="")
				self.window.pages["content_page"].tkraise()
			else:
				# print("denied")
				self.window.pages["login_page"].label_error.configure(text="Login Failed")
		else:
			# print("denied")
			self.window.pages["login_page"].label_error.configure(text="Login Failed")

		self.window.pages['login_page'].entry_username_var.set("")
		self.window.pages['login_page'].entry_password_var.set("")
		self.window.pages['login_page'].entry_username.focus()


	def click_logout_button(self):
		self.window.pages["login_page"].tkraise()

my_app = App()
my_app.run()