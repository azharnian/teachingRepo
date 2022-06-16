from tkinter import Tk, Frame, Label
from PIL import Image, ImageTk

window = Tk()

my_image = Image.open("treasuremap.jpg")
my_image = ImageTk.PhotoImage(my_image)
my_image_label = Label(window, image=my_image)
my_image_label.pack()

window.mainloop()