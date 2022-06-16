from datetime import datetime

from tkinter import Tk, Label, Entry, Button, StringVar, Frame, Radiobutton
from tkinter.ttk import Combobox

window = Tk()
window.title("Form Siswa Ignatius Global School")
window.geometry("300x400")

title_label = Label(window, text="Form Pendaftaran")
title_label.grid(row=0, column=0, columnspan=2, sticky="nesw")

name_label = Label(window, text="Nama :")
name_label.grid(row=1, column=0, sticky="e")

name_entry_frame = Frame(window)
name_entry_frame.grid(row=1, column=1, sticky="nsew")
#name_entry.grid(row=1, column=1, sticky="w")
name_entry = Entry(name_entry_frame)
name_entry.pack(fill="both", expand=True)

birth_place_label = Label(window, text="Tempat Lahir :")
birth_place_label.grid(row=2, column=0, sticky="e")


birth_place_frame = Frame(window)
birth_place_frame.grid(row=2, column=1, sticky="nsew")
birth_place_entry = Entry(birth_place_frame)
#birth_place_entry.grid(row=2, column=1, sticky="w")
birth_place_entry.pack(fill="both", expand=True)

birth_date_label = Label(window, text="Tanggal Lahir :")
birth_date_label.grid(row=3, column=0, sticky="e")

birth_date_frame = Frame(window)
birth_date_frame.grid(row=3, column=1, sticky="nsew")


day_combobox = Combobox(birth_date_frame, width=2)
day_combobox['values'] = list(range(1, 32))
day_combobox.current(datetime.now().day - 1)
#day_combobox.grid(row=0, column=0)
day_combobox.pack(side="left")


month_combobox = Combobox(birth_date_frame, width=9) #dropdown
month_combobox['values'] = ('Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember')
month_combobox.current(datetime.now().month - 1)
#month_combobox.grid(row=0, column=1)
month_combobox.pack(side="left", expand=True)


year_combobox = Combobox(birth_date_frame, width=5)
year_combobox['values'] = list(range(1990, datetime.now().year+1))
year_combobox.current(0)
#year_combobox.grid(row=0, column=2)
year_combobox.pack(side="left")

sex_label = Label(window, text="Jenis Kelamin :")
sex_label.grid(row=4, column=0, sticky="e")

sexFrame = Frame(window)
sexFrame.grid(row=4, column=1, sticky="w")

maleRadio = Radiobutton(sexFrame, text="Laki-laki")
femaleRadio = Radiobutton(sexFrame, text="Perempuan")

maleRadio.pack(side="left", expand=True)
femaleRadio.pack(side="left", expand=True)

save_button = Button(window, text="Simpan Data")
save_button.grid(row=5, column=0, columnspan=2)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=3)
# window.grid_rowconfigure(1, weight=1)
# window.grid_rowconfigure(2, weight=1)
# window.grid_rowconfigure(3, weight=1)
# window.grid_rowconfigure(4, weight=1)
# window.grid_rowconfigure(5, weight=1)

birth_date_frame.grid_columnconfigure(0, weight=1)
birth_date_frame.grid_columnconfigure(1, weight=1)
birth_date_frame.grid_columnconfigure(2, weight=1)


window.mainloop()