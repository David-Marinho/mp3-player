import tkinter as tk
from func import tocar
from func_menu import *


class mp3:
    def __init__(self, root: tk.Tk):
        self.root = root



    def algo(self):
        pass


    def criar_musica(self, musicas):
        global barra, btn
        global i
        eixoY = 30
        barra = tk.PhotoImage(file='imagens/caixas.png')
        for i in range(len(musicas)):
            btn = tk.Button(self.root, image=barra, borderwidth=0, text=musicas[i], bg='#444444')
            btn.place(x=20, y=eixoY)
            eixoY += 90
            btn.bind("<Button-1>", self.escolher_musica)

    def lb_musica(self, texto, eixoY):
        tk.Label().place(x=30, y=eixoY + 20)

    def escolher_musica(self, event=None):
        tocar(event.widget['text'])
