from pygame import mixer


class Musicas:
    def __init__(self, nome: str, tempo: float, banda: str, ligado: bool):
        self.nome = nome
        self.tempo = tempo
        self.banda = banda
        self.ligado = ligado

    def tocar(self):
        mixer.init()
        mixer.music.load(f'musicas/{self.nome}')
        mixer.music.play()

    def pausar(self):
        mixer.music.pause()

    def restart(self):
        mixer.music.unpause()

    def repetir(self):
        mixer.music.load(f'musicas/{self.nome}')

    def ordem_aleatoria(self):
        pass

"""    def __init__(self, raiz, nome, img):
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
        tocar(event.widget['text'], self.raiz)"""
