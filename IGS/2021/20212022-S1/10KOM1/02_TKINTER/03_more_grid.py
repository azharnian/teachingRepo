from tkinter import Tk, Label, Entry, Button, StringVar

window = Tk()
window.title("More Grid")
window.geometry("500x500") # widthxheight

title = Label(window, text="Login")
title.grid(row=0, column=0, columnspan=2)

sub_title = Label(window, text="Masuk ke Aplikasi")
sub_title.grid(row=1, column=0, columnspan=2)

username_label = Label(window, text="Username")
username_label.grid(row=2, column=0)

username_entry = Entry(window)
username_entry.grid(row=2, column=1)

# password_label = ...

# password_entry = ...

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=3)


window.mainloop()