from tkinter import Tk, Label, Entry, Button, StringVar

def change_text_label():
	label.configure(text=entry_variable.get())

window = Tk()

label = Label(window, text="I Love You 3000")
label.grid()

entry_variable = StringVar()
entry = Entry(window, textvariable=entry_variable)
entry.grid()

button = Button(window, text="submit!", command=change_text_label)
button.grid()

window.mainloop()