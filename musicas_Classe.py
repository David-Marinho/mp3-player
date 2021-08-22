from tkinter import *
from func import tocar

y = 0


class bt_musicas:
    def __init__(self, raiz, nome, img):
        self.raiz = raiz
        self.nome = nome
        self.img = img

    def criar_bt(self):
        global y
        botao = Button(self.raiz, text=self.nome, image=self.img, borderwidth=0)
        botao.bind('<Button-1>', self.bt_click)
        botao.grid(column=0, row=y, padx=10, pady=10)
        self.criar_lb()
        y += 1

    def criar_lb(self):
        Label(self.raiz, text=self.nome, font='20', bg='#444444').grid(column=0, row=y)

    def bt_click(self, event=None):
        tocar(event.widget['text'])
