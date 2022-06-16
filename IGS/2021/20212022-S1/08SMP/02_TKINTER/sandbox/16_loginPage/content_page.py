from tkinter import Frame, Label, Entry, Button, StringVar
from PIL import Image, ImageTk


class ContentPage(Frame):

	def __init__(self, parent, window, *args, **kwargs):

		super().__init__(parent, *args, **kwargs)
		#self.pack(fill="both", expand=True)
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)
		
		#self.configure(bg="green")
		self.app = window.app
		self.settings = window.settings

		self.main_frame = Frame(self, bg="black")
		self.main_frame.pack(fill="both", expand=True)

		self.main_frame.grid_rowconfigure(0, weight=1)
		self.main_frame.grid_rowconfigure(1, weight=2)
		self.main_frame.grid_columnconfigure(0, weight=1)

		self.logout_button = Button(self.main_frame, text="logout please!", command=self.app.click_logout_button)
		self.logout_button.grid(row=0, column=0, sticky="nsew")

	