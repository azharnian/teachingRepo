from tkinter import Tk, Label, Button, Frame

window = Tk()
window.title("Learning More about Pack Method")
window.geometry("300x400+500+500")

button0 = Button(window, text="CLICK ME!", bg="purple")
button0.pack(side="left") # "top", "right", "bottom", "left"

button1 = Button(window, text="CLICK AGAIN!", bg="pink")
button1.pack(side="left")

button2 = Button(window, text="CLICK MORE!", bg="blue")
button2.pack(side="bottom")

button3 = Button(window, text="CLICK YOU!", bg="red")
button3.pack(side="right")


window.mainloop()