from tkinter import Tk, Frame, Label
from PIL import Image, ImageTk #PIL === pillow

from settings import Settings # from settings.py file import Settings Class


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

		self.pages["page0"] = Frame(self.container, bg="green")
		self.pages["page0"].pack(fill="both", expand=True)

		# self.main_frame = Frame(self.pages["page0"], bg="grey")
		# self.main_frame.pack(fill="both", expand=True)

		self.my_image = Image.open("treasuremap.jpg")
		self.my_image = ImageTk.PhotoImage(self.my_image)
		self.my_image_label = Label(self.pages["page0"], image=self.my_image)
		self.my_image_label.pack(fill="both", expand=True)


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