from tkinter import *
from tkinter import filedialog

window = Tk()

window.title("File Sorter")
window.minsize(750, 500)

def path_browse():
    folder_name = filedialog.askdirectory()
    path_form.delete(0, END)
    path_form.insert(0, folder_name)

path_label = Label (window, text="Select a path to clean up:").place(x = 40, y = 60)
path_form = Entry (window, width = 30)
path_form.place(x = 40, y = 90)
path_button = Button(window, text="Browse", command=path_browse).place(x = 270, y = 90)


window.mainloop()