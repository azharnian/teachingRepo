from tkinter import Frame, Label, Entry, Button, StringVar
from PIL import Image, ImageTk


class LoginPage(Frame):

	def __init__(self, parent, Window, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		# self.pack(fill="both", expand=True)
		self.app = Window.app
		self.grid(row=0, column=0, sticky="nsew")
		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		#self.configure(bg="green")
		self.settings = Window.settings

		self.main_frame = Frame(self, bg="white")
		self.main_frame.pack(fill="both", expand=True)

		self.main_frame.grid_rowconfigure(0, weight=1)
		self.main_frame.grid_rowconfigure(1, weight=2)
		self.main_frame.grid_columnconfigure(0, weight=1)

		self.create_logo_frame()
		self.create_login_frame()

		
	def create_logo_frame(self):
		self.logo_frame = Frame(self.main_frame, bg="white")
		self.logo_frame.grid(row=0, column=0, sticky="nsew")

		my_image = Image.open("logo.png")
		my_image_w, my_image_h = my_image.size
		#print(my_image_w, my_image_h)
		ratio  = my_image_w/self.settings.width*3
		new_size = (int(my_image_w//ratio), int(my_image_h//ratio))
		my_image = my_image.resize(new_size)
		self.my_image = ImageTk.PhotoImage(my_image)
		self.my_image_label = Label(self.logo_frame, image=self.my_image, bg="white")
		self.my_image_label.pack(fill="both", expand=True)


	def create_login_frame(self):
		self.login_frame = Frame(self.main_frame, bg="white")
		self.login_frame.grid(row=1, column=0, sticky="nsew", padx=30)

		self.login_frame.grid_columnconfigure(0, weight=1)
		self.login_frame.grid_columnconfigure(1, weight=2)

		self.label_username = Label(self.login_frame, text="Nama Pengguna", font=("Arial", 12), bg="white")
		self.label_username.grid(row=0, column=0, sticky="w")


		self.entry_username_frame = Frame(self.login_frame)
		self.entry_username_frame.grid(row=0, column=1, sticky="nsew")

		self.entry_username_var = StringVar()
		self.entry_username = Entry(self.entry_username_frame, font=("Arial", 12), textvariable=self.entry_username_var)
		self.entry_username.pack(fill="both", expand=True)

		self.label_password = Label(self.login_frame, text="Kata Sandi", font=("Arial", 12), bg="white")
		self.label_password.grid(row=1, column=0, sticky="w")


		self.entry_password_frame = Frame(self.login_frame)
		self.entry_password_frame.grid(row=1, column=1, sticky="nsew")

		self.entry_password_var = StringVar()
		self.entry_password = Entry(self.entry_password_frame, font=("Arial", 12), show="*", textvariable=self.entry_password_var)
		self.entry_password.pack(fill="both", expand=True)

		self.login_button = Button(self.login_frame, text="Masuk", font=("Arial", 12), command=self.app.click_login_button)
		self.login_button.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=100, pady=10)


	











