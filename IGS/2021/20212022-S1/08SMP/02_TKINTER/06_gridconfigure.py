from tkinter import Tk, Button, Frame

window = Tk()
window.title("Grid")
window.geometry("300x400")

frame0 = Frame(window, bg="yellow")
frame0.grid(row=0, column=0, sticky="nsew")

frame1 = Frame(window, bg="green")
frame1.grid(row=0, column=1, sticky="nsew")

frame2 = Frame(window, bg="red")
frame2.grid(row=0, column=2, sticky="nsew")

frame3 = Frame(window, bg="blue")
frame3.grid(row=1, columnspan=3, sticky="nesw")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

window.mainloop()