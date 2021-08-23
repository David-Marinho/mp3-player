from func import *

class menu():
    def __init__(self, raiz):
        self.raiz = raiz

    def criar_menu(self):
        global barra_img
        barra_img = PhotoImage(file='imagens/barra.png')
        Label(self.raiz, image=barra_img, borderwidth=0).place(x=0, y=410)
        self.criar_botoes()

    def criar_botoes(self):
        global image1, image2, image3

        image1 = PhotoImage(file='imagens/botao pause.png')

        pausePlay = Button(self.raiz, image=image1, borderwidth=0, bg='#444444', command=lambda: tocando(pausePlay))
        pausePlay.place(x=390, y=450)
