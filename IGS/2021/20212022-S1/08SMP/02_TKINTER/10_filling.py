from tkinter import Tk, Label, Button, Frame

window = Tk()
window.title("Learning More about Pack Method")
window.geometry("300x400+500+500")

button0 = Button(window, text="CLICK ME!", bg="purple")
button0.pack(side="left", fill="both", expand=True) # "top", "right", "bottom", "left"

button1 = Button(window, text="CLICK AGAIN!", bg="pink")
button1.pack(side="left", fill="both", expand=True) # x, y, both


"""
side : left / right -> fill : y (mengisi ruang sisa di xb.y)
side : top / bottom -> fill : x (mengisi ruang sisa di sb.x)
fill : both, expand = True (mengisi ruang sisa ke arah sb. x dan y)
"""


window.mainloop()