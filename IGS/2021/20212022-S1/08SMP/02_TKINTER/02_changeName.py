from tkinter import Tk, Label, Button, Entry, StringVar

def change_text_label():
	label.configure(text=entry_var.get())

window = Tk()

label = Label(window, text="Anas Azhar")
label.grid()

entry_var = StringVar() #IntVar
entry = Entry(window, textvariable=entry_var)
entry.grid()

button = Button(window, text="change!", command=change_text_label)
button.grid()

window.mainloop() # 80 Mhz -> 80 * 10^6 / second