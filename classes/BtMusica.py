from Botao import Botao
from Musicas import Musicas


class BtMusica(Botao):
    def __init__(self, bg: str, fg: str, altura: int, largura: int, musica: Musicas):
        super().__init__(bg, fg, altura, largura)
        self.musica = musica

    def OnClick(self):
        self.musica.tocar()
    

"""from pygame import mixer

reproduzindo = False


def tocar(musica, raiz):
    global reproduzindo, faixa
    mixer.init()
    mixer.music.load(f'musicas/{musica}')
    faixa = mixer.music.play()
    Label(raiz, text=musica, bg='#444444', font=16).place(x=200, y=420)
    reproduzindo = True


def tocando(button):
    global reproduzindo
    if reproduzindo:
        pausar(button)
        mixer.music.pause()

    else:
        despausar(button)
        mixer.music.unpause()


def pausar(button):
    global botao_play, reproduzindo
    botao_play = PhotoImage(file='imagens/botao play.png')
    button['image'] = botao_play
    reproduzindo = False


def despausar(button):
    global botao_pause, reproduzindo
    botao_pause = PhotoImage(file='imagens/botao pause.png')
    button['image'] = botao_pause
    reproduzindo = True"""
