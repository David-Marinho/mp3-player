from os import listdir
from pygame import mixer
from GUI import *

musicas = list()
tocando = True
janela = tela


for i in listdir('musicas'):
    if 'mp3' in i.split('.'):
        print('ok')
        musicas.append(i)
        janela.add_btn(i, janela)


def tocar(faixa):
    mixer.music.load(f'musicas/{faixa}')
    mixer.music.play()

"""
elif escolha == 'next':
mixer.music.stop()
musica +=1
mixer.music.load(f'musicas/{lista[musica]}')
mixer.music.play()
print(f'tocando: {lista[musica]}')
"""