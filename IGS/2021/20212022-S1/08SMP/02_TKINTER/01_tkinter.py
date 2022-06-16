#import tkinter
from tkinter import Tk, Label, Entry, Button

#nama kelas untuk window (jendela aplikasi) -> Tk()
window = Tk() # willey = Dog()

label = Label(window, text="My First Tkinter")
label.grid()

label1 = Label(window, text="Okey I'm fine")
label1.grid()

entry = Entry(window)
entry.grid()

button = Button(window, text="submit!")
button.grid()

window.mainloop() # willey.show() (method)