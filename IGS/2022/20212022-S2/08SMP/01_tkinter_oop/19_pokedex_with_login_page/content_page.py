from tkinter import Frame, Label, Entry, Button, StringVar, LabelFrame
from tkinter.ttk import Notebook, Combobox
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
		self.footer_frame = LabelFrame(self.main_frame, bg="white", text="More information")
		self.footer_frame.grid(row=1, column=0, sticky="nsew")

		self.footer_frame.grid_columnconfigure(0, weight=1)
		self.footer_frame.grid_rowconfigure(0, weight=2)
		self.footer_frame.grid_rowconfigure(1, weight=1)

		self.type_frame = Frame(self.footer_frame, bg="black")
		self.type_frame.grid(row=0, column=0, sticky="nsew")

		self.tab_notebook = Notebook(self.type_frame)

		self.type_tab = Frame(self.tab_notebook, bg="white")
		self.weakness_tab = Frame(self.tab_notebook, bg="white")
		
		self.type_tab.grid_columnconfigure(0, weight=1)
		self.weakness_tab.grid_columnconfigure(0, weight=1)

		self.tab_notebook.add(self.type_tab, text="Type")
		self.tab_notebook.add(self.weakness_tab, text="Weakness")

		self.tab_notebook.pack(fill="both", expand=True)

		self.types = [{"type":"fire", "color":"orange"}, {"type":"wind", "color":"pink"}]
		self.type_tabs = []

		self.weaknesses = [{"weakness":"water", "color":"blue"}, {"weakness":"ground", "color":"brown"}, {"weakness":"rock", "color":"black"}]
		self.weakness_tabs = []


		for row in range(len(self.types)):
			label = Label(self.type_tab, text=self.types[row]["type"], font=("Arial", 16, "bold"), fg="white", bg=self.types[row]["color"])
			label.grid(row=row, column=0, sticky="nsew", padx=15, pady=10)
			self.type_tabs.append(label)

		for row in range(len(self.weaknesses)):
			label = Label(self.weakness_tab, text=self.weaknesses[row]["weakness"], font=("Arial", 16, "bold"), fg="white", bg=self.weaknesses[row]["color"])
			label.grid(row=row, column=0, sticky="nsew", padx=15, pady=10)
			self.weakness_tabs.append(label)


		self.comboFrame = Frame(self.footer_frame)
		self.comboFrame.grid(row=1, column=0, sticky="nsew")

		self.combobox = Combobox(self.comboFrame, font=("Arial", 25, "bold"), justify="center", state="readonly", background="white")
		self.combobox["values"] = ("Charmender", "Venusaur", "Charmeleon")
		self.combobox.current(0)
		self.combobox.pack(fill="both", expand=True)

		self.text_footer = Label(self.comboFrame, text="Pokemdex Alamanac 2021", bg="white")
		self.text_footer.pack(fill="x")

		










