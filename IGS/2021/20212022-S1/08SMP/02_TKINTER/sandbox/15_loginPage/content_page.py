from tkinter import Tk, Frame

class ContentPage(Frame):


	def __init__(self, parent, App, **kwargs):
		super().__init__(parent, **kwargs)
		self.pack(fill="both", expand=True)
		self.settings = App.settings

		self.main_frame = Frame(self, bg="white")
		self.main_frame.pack(fill="both", expand=True)