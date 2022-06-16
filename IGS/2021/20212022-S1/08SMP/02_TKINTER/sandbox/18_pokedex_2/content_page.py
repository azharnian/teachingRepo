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

		#self.logout_button = Button(self.main_frame, text="Logout Please !!", command=self.app.click_logout_button)
		#self.logout_button.grid(row=0, column=0, sticky="nesw")

		self.create_header_frame()
		self.create_body_frame()

	def create_header_frame(self):
		self.header_frame = LabelFrame(self.main_frame, bg="grey", text="Pokodex by Pokemon")
		self.header_frame.grid(row=0, column=0, sticky="nsew")

		self.header_frame.grid_columnconfigure(0, weight=3)
		self.header_frame.grid_columnconfigure(1, weight=2)
		self.header_frame.grid_rowconfigure(0, weight=2)
		self.header_frame.grid_rowconfigure(1, weight=5)

		self.title_frame = Frame(self.header_frame, bg="grey")
		self.title_frame.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

		self.title_character_label = Label(self.title_frame, text="Charmender #004", font=("Arial", 30, "bold"), bg="grey", fg="white")
		self.title_character_label.pack(fill="both", expand=True)

		self.photo_frame = Frame(self.header_frame, bg="grey")
		self.photo_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

		character_image = Image.open("01.png")
		character_image_w, character_image_h = character_image.size
		#print(my_image_w, my_image_h)
		ratio = character_image_h/self.settings.width*2.5
		new_size = (int(character_image_w//ratio), int(character_image_h//ratio))
		character_image = character_image.resize(new_size)
		self.character_image = ImageTk.PhotoImage(character_image)
		self.character_image_label = Label(self.photo_frame, image=self.character_image, bg="grey")
		self.character_image_label.pack(fill="both", expand=True)

		self.info_frame = Frame(self.header_frame, bg="grey")
		self.info_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

		self.description_label = Label(self.info_frame, text='"It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail."', wraplength=150, font=("Arial", 14), bg="grey", fg="white", justify="left")
		self.description_label.pack(fill="x", padx=10, pady=10)

		self.more_info_frame = Frame(self.info_frame, bg="grey")
		self.more_info_frame.pack(fill="both", expand=True, padx=10, pady=10)

		self.heigth_label = Label(self.more_info_frame, text="Height\t: 2' 00'' ", font=("Arial", 14), bg="grey", fg="white", justify="left")
		self.heigth_label.grid(row=0, column=0, sticky="w")

		self.weight_label = Label(self.more_info_frame, text="Weight\t: 18.7 lbs ", font=("Arial", 14), bg="grey", fg="white", justify="left")
		self.weight_label.grid(row=1, column=0, sticky="w")

		self.category_label = Label(self.more_info_frame, text="Category\t: Lizard ", font=("Arial", 14), bg="grey", fg="white", justify="left")
		self.category_label.grid(row=2, column=0, sticky="w")

		self.ability_label = Label(self.more_info_frame, text="Ability\t: Blaze ", font=("Arial", 14), bg="grey", fg="white", justify="left")
		self.ability_label.grid(row=3, column=0, sticky="w")


	def create_body_frame(self):
		self.body_frame = LabelFrame(self.main_frame, bg="white", text="More Information")
		self.body_frame.grid(row=1, column=0, sticky="nsew")

		self.body_frame.grid_rowconfigure(0, weight=2)
		self.body_frame.grid_rowconfigure(1, weight=1)
		self.body_frame.grid_columnconfigure(0, weight=1)

		self.type_frame = Frame(self.body_frame, bg="white")
		self.type_frame.grid(row=0, column=0, sticky="nsew")

		self.tab_control = Notebook(self.type_frame)

		self.type_tab = Frame(self.tab_control, bg="white")
		self.weakness_tab = Frame(self.tab_control, bg="white")

		self.type_tab.grid_columnconfigure(0, weight=1)
		self.weakness_tab.grid_columnconfigure(0, weight=1)

		self.tab_control.add(self.type_tab, text="Type")
		self.tab_control.add(self.weakness_tab, text="Weakness")

		self.tab_control.pack(fill="both", expand=True)

		self.type_text = Label(self.type_tab, text="Fire", font=("Arial", 16, "bold"), fg="white", bg="orange")
		self.type_text.grid(row=0, column=0, sticky="nsew", padx=15, pady=10)


		self.weakness_text1 = Label(self.weakness_tab, text="Water", font=("Arial", 16, "bold"), fg="white", bg="blue")
		self.weakness_text1.grid(row=0, column=0, sticky="nsew", padx=15, pady=10)

		self.weakness_text2 = Label(self.weakness_tab, text="Rock", font=("Arial", 16, "bold"), fg="white", bg="brown")
		self.weakness_text2.grid(row=0, column=1, sticky="nsew", padx=15, pady=10)

		self.weakness_text3 = Label(self.weakness_tab, text="Ground", font=("Arial", 16, "bold"), fg="white", bg="grey")
		self.weakness_text3.grid(row=0, column=2, sticky="nsew", padx=15, pady=10)

		self.footer_frame = Frame(self.body_frame, bg="grey")
		self.footer_frame.grid(row=1, column=0, sticky="nsew")

		self.main_combobox = Combobox(self.footer_frame, font=("Arial", 25, "bold"), justify="center", state="readonly")
		self.main_combobox["values"] = ("Charmender", "Venusaur", "Charmeleon")
		self.main_combobox.current(0)
		self.main_combobox.pack(fill="both", expand=True)

		self.text_footer = Label(self.footer_frame, text="Pokodex Almanac 2021", bg="white")
		self.text_footer.pack(fill="x")









