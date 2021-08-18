from pygame import mixer


def tocar(faixa):
    print(f'tocando: {faixa}')
    mixer.music.load(f'musicas/{faixa}')
    mixer.music.play()
