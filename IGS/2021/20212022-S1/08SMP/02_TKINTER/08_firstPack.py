from tkinter import Tk, Label, Button

window = Tk()
window.title("Pack Method")
window.geometry("300x400")

name_label = Label(window, text="Anas Azhar")
name_label.pack()

birth_place_label = Label(window, text="Surabaya")
birth_place_label.pack()

hobby_label = Label(window, text="Nothing")
hobby_label.pack()

coding_button = Button(window, text="Coding Now!")
coding_button.pack()

#side , fill , expand

window.mainloop()
