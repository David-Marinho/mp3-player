import tkinter as tk


def criar_Janela():
    root = tk.Tk()
    root.geometry('850x500')
    root.config(bg='#fff')
    return root

"""def pause_play():
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


def mudar_logo(status):
    global pause_logo
    if status == 'play':
        pause_logo['file'] = 'imagens/botao play.png'


    else:
        pause_logo['file'] = 'imagens/botao pause.png'

    pausePlay.config(image=pause_logo)"""
