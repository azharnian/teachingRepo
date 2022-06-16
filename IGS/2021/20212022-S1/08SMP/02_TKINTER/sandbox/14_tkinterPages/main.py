from tkinter import Tk, Frame, Label
from PIL import Image, ImageTk #PIL === pillow

from settings import Settings # from settings.py file import Settings Class


class Window(Tk):

	def __init__(self, MyApp, *args, **kwargs):
		super().__init__(*args, **kwargs) # to inherit properly from Tk
		self.settings = MyApp.settings
		self.title(self.settings.title)
		self.geometry(f"{self.settings.width}x{self.settings.height}")

		# self.container = Frame(self, bg="grey")
		# self.container.pack(fill="both",expand=True)

		# self.page0 = Frame(self.container)
		# self.page0.grid()

		# self.container.grid_columnconfigure(0, weight=1)
		# self.container.grid_rowconfigure(0, weight=1)

		# my_image = Image.open("win.png")
		# my_images = ImageTk.PhotoImage(my_image)
		# self.my_image_label = Label(self.page0, image=my_images)
		# self.my_image_label.pack()

		self.container = Frame(self, bg="red")
		self.container.pack(fill="both", expand=True)

		self.container.grid_rowconfigure(0, weight=1)
		self.container.grid_columnconfigure(0, weight=1)

		self.pages = {}

		self.pages['page01'] = Frame(self.container, bg="green")
		self.pages['page01'].pack(fill="both", expand=True)

		# self.pages['page01'].grid_rowconfigure(0, weight=1)
		# self.pages['page01'].grid_columnconfigure(0, weight=1)
		#self.pages['page01'].grid(row=0, column=0)

		self.main_frame = Frame(self.pages['page01'], bg="grey")
		self.main_frame.pack(fill="both", expand=True)


		self.my_image = Image.open("treasuremap.jpg")
		self.my_image = ImageTk.PhotoImage(self.my_image)
		self.my_image_label = Label(self.main_frame, image=self.my_image)
		self.my_image_label.pack(fill="both", expand=True)

		# 


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