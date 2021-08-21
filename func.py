import tkinter as tk
from pygame import mixer


def criar_Janela():
    root = tk.Tk()
    root.geometry('850x500')
    root.config(bg='#fff')
    return root


def musicas(arq):
    lista = list()
    for i in range(len(arq)):
        if 'mp3' in arq[i].split('.'):
            lista.append(arq[i])

    return lista


def tocar(musica):
    mixer.init()
    mixer.music.load(f'musicas/{musica}')
    mixer.music.play()


def pausar():
    mixer.pause()


def despausar():
    mixer.unpause()

