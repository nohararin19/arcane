import csv
from tkinter import *

filepath = 'csv/video_games.csv'

File = open(filepath)
Reader = csv.reader(File)
Data = list(Reader)
del (Data[0])

list_of_entries = []
for x in list(range(0, len(Data))):
    list_of_entries.append(Data[x][0])

root = Tk()
root.geometry('280x300')
var = StringVar(value=list_of_entries)
listbox1 = Listbox(root, listvariable=var)
listbox1.grid(row=0, column=0)


def update():
    index = listbox1.curselection()[0]
    namelabel2.config(text=Data[index][0])
    genrelabel2.config(text=Data[index][5])
    publisherlabel2.config(text=Data[index][7])
    pricelabel2.config(text=Data[index][10])

    return None


button1 = Button(root, text="Update", command=update)
button1.grid(row=5, column=0)

namelabel = Label(root, text="Название").grid(row=1, column=0, sticky="w")
genrelabel = Label(root, text="Жанр").grid(row=2, column=0, sticky="w")
publisherlabel = Label(root, text="Издатель").grid(row=3, column=0, sticky="w")
pricelabel = Label(root, text="Цена (в $)").grid(row=4, column=0, sticky="w")

namelabel2 = Label(root, text="")
namelabel2.grid(row=1, column=1, sticky="w")
genrelabel2 = Label(root, text="")
genrelabel2.grid(row=2, column=1, sticky="w")
publisherlabel2 = Label(root, text="")
publisherlabel2.grid(row=3, column=1, sticky="w")
pricelabel2 = Label(root, text="")
pricelabel2.grid(row=4, column=1, sticky="w")

root.mainloop()
