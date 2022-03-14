from tkinter import *
from tkinter import messagebox


class mobb(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.action_menu()

    def action_menu(self):
        self.pack(fill=BOTH, expand=1)
        self.btn_opn = Button(text="Выбрать игру", height=5, width=25, command=self.game_selector)
        self.btn_opn.place(x=410, y=350)

        self.pack(fill=BOTH, expand=1)
        self.btn_exit = Button(text='Выход', height=3, width=15, command=self.close)
        self.btn_exit.place(x=450, y=500)

    def close(self):
        if messagebox.askyesno('Выход', 'Вы уверены?'):
            self.parent.destroy()

    def game_selector(self):
        game = Toplevel(root)
        game.title('Игровой терминал MOBB')
        game.geometry('1024x768')


if __name__ == '__main__':
    root = Tk()
    root.title('Игровой терминал MOBB')
    root.geometry('1024x768')
    root.iconbitmap('img/mobb.ico')
    bg = PhotoImage(file='img/bg.png')
    canvas1 = Canvas(root, width=1024, height=768)
    canvas1.pack(fill='both', expand=True)
    canvas1.create_image(0, 0, image=bg, anchor='nw')
    app = mobb(root)
    root.mainloop()
