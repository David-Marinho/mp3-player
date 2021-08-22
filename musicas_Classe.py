from tkinter import *

eixoY = 20
corfundo = '#444444'


class musicas:
    def __init__(self, raiz, nome, img):
        self.raiz = raiz
        self.nome = nome
        self.img = img

    def criar_bt(self):
        global eixoY
        botao = Button(self.raiz, text=self.nome, image=self.img, borderwidth=0)     #        bt = Button().bind().place()
        botao.bind('<Button-1>', self.tocar_musica)
        botao.place(x=20, y=eixoY)

        self.criar_lb()
        eixoY += 90

    def criar_lb(self):
        Label(self.raiz, text=self.nome, font='20', bg=corfundo).place(x=40, y=eixoY+20)

    def tocar_musica(self, event=None):
        print(f'tocando: {event.widget["text"]}')
