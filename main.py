from pygame import mixer
from os import listdir
from tkinter import *

janela = Tk()
janela.geometry("800x400")

musicas = dict()
arq = listdir('musicas')
numero_Faixa = 0
tocando = True

mixer.init()


def mudar_logo(status):
    global pause_logo
    if status == 'play':
        pause_logo['file'] = 'outline_play_arrow_black_24dp.png'


    else:
        pause_logo['file'] = 'outline_pause_black_24dp.png'

    pausePlay.config(image=pause_logo)


def pause_play():
    global tocando
    global pause_logo
    if tocando:
        mixer.music.pause()
        tocando = False
        mudar_logo('play')


    else:
        mixer.music.unpause()
        tocando = True
        mudar_logo('pause')



def tocar(faixa):
    mixer.music.load(f'musicas/{faixa}')
    mixer.music.play()


def exibir_botao(musica):
    bt = Button(janela, text=musica, command = lambda: tocar(musica))
    bt.grid(sticky='w')


for i in range(len(arq)):
    if 'mp3' in arq[i].split('.'):
        musicas[i] = arq[i]
        exibir_botao(musicas[i])
pause_logo = PhotoImage(file='outline_pause_black_24dp.png')

pausePlay = Button(janela, command = lambda: pause_play(), image=pause_logo)
pausePlay.place(x=240, y=350)






"""
while True:
    escolha = str(input('digite: \n\nstop \nnext \npause \ndespause \nsair \n\noque voce quer fazer? '))

    elif escolha == 'next':
        mixer.music.stop()
        musica +=1
        mixer.music.load(f'musicas/{lista[musica]}')
        mixer.music.play()
        print(f'tocando: {lista[musica]}')
"""

janela.mainloop()
