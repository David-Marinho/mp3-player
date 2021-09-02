from func import *


class menu():
    def __init__(self, raiz):
        self.raiz = raiz

    def criar_menu(self):
        Label(self.raiz, bg='#65B5FF', borderwidth=0, height=8, width=122).place(x=0, y=390)
        self.criar_botoes()

    def criar_botoes(self):
        global image1, image2, image3

        image1 = PhotoImage(file='imagens/botao pause.png')

        pausePlay = Button(self.raiz, image=image1, borderwidth=0, bg='#65B5FF', command=lambda: tocando(pausePlay))
        pausePlay.place(x=390, y=400)
