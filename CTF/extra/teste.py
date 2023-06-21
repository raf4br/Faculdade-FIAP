from tkinter import *
from tkinter import messagebox
from random import randint


class Cracker:

    def __init__(self, master):
        self.NUMBERS = 8
        self.frames = [[], [], [], []]
        self.imageplaces = []
        self.labels = []
        self.cbs = []
        for i in range(4):
            for j in range(self.NUMBERS):
                self.frames[i].append(
                    Frame(master, width=100, height=100, bd=5, relief='ridge'))
                self.frames[i][j].grid(row=i, column=j)
        labels = [str(x).zfill(2) for x in range(1, 9)]
        for i in range(self.NUMBERS):
            self.imageplaces.append(
                Label((self.frames[0][i]),
                      text=str(randint(1, 6)),
                      font=('Arial Bold', 24)))
            self.imageplaces[i].value = int(self.imageplaces[i].cget("text"))
            self.imageplaces[i].pack()
            state = BooleanVar()
            self.cbs.append(Checkbutton((self.frames[2][i]), variable=state))
            self.cbs[i].state = state
            self.cbs[i].pack()
            self.labels.append(
                Label((self.frames[1][i]),
                      text=(labels[i]),
                      font=('Arial Bold', 14)))
            self.labels[i].pack()

        self.br = Button((self.frames[3][0]),
                         text='Random',
                         font=('Arial Bold', 24),
                         command=(self.randomize))
        self.br.pack()
        self.bc = Button((self.frames[3][1]),
                         text='Check',
                         font=('Arial Bold', 24),
                         command=(self.checkserial))
        self.bc.pack()

    def randomize(self):
        for i in range(self.NUMBERS):
            if not self.cbs[i].state.get():
                self.imageplaces[i]['text'] = str(randint(1, 6))
                self.imageplaces[i].value = int(
                    self.imageplaces[i].cget("text"))

    def checkserial(self):
        d1, d2, d3, d4, d5, d6, d7, d8 = [
            self.imageplaces[i].value for i in range(self.NUMBERS)
        ]
        if d1 + d3 + d5 + d7 == 12 and d2 + d4 + d6 + d8 == 11 and d2 * d3 * d7 == 24 and d1 * d2 * d3 * d5 == 60 and d7 - d2 + d3 - d4 == 0 and d6 + d1 + d8 == 10 and d8 > 3:
            flag = f"fiap{{{d1}{d2}{d3}{d4}{d5}{d6}{d7}{d8}}}"
            messagebox.showinfo(title='Parabéns!', message=f"A flag é {flag}")
        else:
            messagebox.showerror(title='Erro!',
                                 message='Erro na Verificação do Serial.')


def main():
    root = Tk()
    Cracker(root)
    root.mainloop()


if __name__ == "__main__":
    main()
