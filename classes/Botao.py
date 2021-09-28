class Botao():
    def __init__(self, bg: str, fg: str, altura: int, largura: int):
        self.bg = bg
        self.fg = fg
        self.altura = altura
        self.largura = largura






""" 
 def __init__(self, raiz):
     self.raiz = raiz

 def criar_menu(self, altura, largura):
     global barra_img
     barra_img = PhotoImage(file='imagens/barra.png')
     Label(self.raiz, image=barra_img, borderwidth=0).place(x=0, y=altura-177)
     self.criar_botoes(altura, largura)

 def criar_botoes(self, altura, largura):
     global image1, image2, image3

     image1 = PhotoImage(file='imagens/botao pause.png')

     pausePlay = Button(self.raiz, image=image1, borderwidth=0, bg='#65B5FF', command=lambda: tocando(pausePlay))
     pausePlay.place(x=largura/2, y=altura-170)
"""