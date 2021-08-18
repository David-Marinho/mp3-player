from pygame import mixer
from os import listdir
from func import *
from estilo import menu

musicas = list()
lista = ['stop', 'next', 'pause', 'despause', 'sair']
mixer.init()
cont = 1

for i in listdir('musicas'):
    if 'mp3' in i.split('.'):
        musicas.append(i)
        cont += 1
menu(musicas)

musica = int(input('digite o numero da musica que voce quer escutar: ')) - 1
tocar(lista[musica])

while True:
    menu(lista)
    escolha = int(input('digite um numero: '))

    if escolha == 1:
        mixer.music.stop()

    elif escolha == 2:
        mixer.music.stop()
        musica += 1
        mixer.music.load(f'musicas/{lista[musica]}')
        mixer.music.play()
        print(f'tocando: {lista[musica]}')

    elif escolha == 3:
        mixer.music.pause()

    elif escolha == 4:
        mixer.music.unpause()

    elif escolha == 5:
        mixer.music.stop()
        break

    else:
        print('comando nao reconhecido. Por favor, tente novamente \n')

    escolha = None
