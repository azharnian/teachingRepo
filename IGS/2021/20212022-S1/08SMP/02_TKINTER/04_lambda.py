from tkinter import Tk, Label, Button

window = Tk()
window.title("My Second Apps")
window.geometry("500x500") # width, height

my_func = lambda : username_label.configure(text="Anas Azhar")

title_label = Label(window,
					text="My Second Apps",
					borderwidth=10,
					relief="groove",
					#width=400,
					#height=5,
					font= ('Arial', 20),
					background="grey",
					foreground="white")
title_label.grid(column=0, row=0, columnspan=2, sticky="nesw") # span 0 dan 1

username_label = Label(window, 
					text="elonmusk",
					borderwidth=10,
					relief="groove",
					width=20,
					#height=2,
					font= ('Comic Sans MS', 20),
					foreground="green")
username_label.grid(column=0, row=1)

groupuser_label = Label(window, 
					text="bazinga",
					borderwidth=10,
					relief="groove",
					width=18,
					#height=2,
					font= ('Comic Sans MS', 20),
					foreground="green")
groupuser_label.grid(column=1, row=1)

button = Button(window,
		text="change!",
		height=2,
		font= ('Comic Sans MS', 20),
		foreground="green",
		#command = lambda : username_label.configure(text="Anas Azhar") # anonymous function
		command=my_func)

button.grid(column=0, row=2, columnspan=2, sticky="nesw")

window.grid_columnconfigure(0, weight=1)

window.mainloop()