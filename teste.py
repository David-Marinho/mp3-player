"""from tkinter import *

dia = {1:'domingo',2:'segunda',3:'terça',4:'quarta',5:'quinta',6:'sexta',7:'sabado'}

i = len(dia)

menu = Tk()
menu.title("Exemplo - Função Exibir Botão")
menu.geometry("500x250+150+150")


def exbir_dia(valor):
    print(valor)
    print(i)


def exbir_botao(i, valor):
    botao = Button(menu, text=dia.get(i), command = lambda: exbir_dia(valor))
    botao.grid()


while i > 0:

    valor = dia.get(i)

    exbir_botao(i, valor)

    i -= 1

menu.mainloop()"""

import tkinter as tk


class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
        self.button1.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __== '__main__':
    main()