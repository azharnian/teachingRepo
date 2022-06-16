from tkinter import Frame, Label, Entry, Button, StringVar
from PIL import Image, ImageTk


class ContentPage(Frame):

	def __init__(self, parent, Window, *args, **kwargs):

		super().__init__(parent, *args, **kwargs)
		#self.pack(fill="both", expand=True)
		self.grid(row=0, column=0, sticky="nesw")
		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		#self.configure(bg="green")
		self.app = Window.app
		self.settings = Window.settings

		self.main_frame = Frame(self, bg="black")
		self.main_frame.pack(fill="both", expand=True)

		self.main_frame.grid_rowconfigure(0, weight=1)
		self.main_frame.grid_rowconfigure(1, weight=2)
		self.main_frame.grid_columnconfigure(0, weight=1)

		self.header_frame()
		self.footer_frame()
	
	def header_frame(self):
		self.header_frame = Frame(self.main_frame, bg="grey")
		self.header_frame.grid(row=0, column=0, sticky="nsew")

		self.header_frame.grid_rowconfigure(0, weight=2)
		self.header_frame.grid_rowconfigure(1, weight=5)
		self.header_frame.grid_columnconfigure(0, weight=3)
		self.header_frame.grid_columnconfigure(1, weight=2)

		self.title_frame = Frame(self.header_frame, bg="red")
		self.title_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

		self.title_label = Label(self.title_frame, text="Charmender 004", font=("Arial", 28, "bold"), bg="grey", fg="white")
		self.title_label.pack(fill="both", expand=True)

		self.photo_frame = Frame(self.header_frame)
		self.photo_frame.grid(row=1, column=0, sticky="nsew")

		char_image = Image.open("01.png")
		char_image_w, char_image_h = char_image.size
		ratio = char_image_h/self.settings.height * 4
		new_size = ( int(char_image_w//ratio), int(char_image_h//ratio) )
		char_image = char_image.resize(new_size)

		self.char_image = ImageTk.PhotoImage(char_image)
		self.char_image_label = Label(self.photo_frame, image=self.char_image, bg="grey")
		self.char_image_label.pack(fill="both", expand=True)


		self.info_frame = Frame(self.header_frame, bg="grey")
		self.info_frame.grid(row=1, column=1, sticky="nsew")

		self.description_label = Label(self.info_frame, text='"It has a preference for hot things.\nWhen it rains, steam is said to spout from the tip of its tail."', wraplength=150, justify="left", font=("Arial"), bg="grey", fg="white")
		self.description_label.pack()

	def footer_frame(self):
		self.footer_frame = Frame(self.main_frame, bg="white")
		self.footer_frame.grid(row=1, column=0, sticky="nsew")







