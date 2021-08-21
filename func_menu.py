from tkinter import *
from func import *

tocando = 'sim'

def criar_menu(raiz):
    global menu_Img
    menu_Img = PhotoImage(file='imagens/barra.png')
    Label(
            raiz,
            image=menu_Img,
            borderwidth=0
         ).place(x=0, y=410)


def criar_pausePlay(raiz):
    global btn_Img
    btn_Img = PhotoImage(file='imagens/botao pause.png')
    return Button(
                    raiz,
                    image=btn_Img,
                    borderwidth=0,
                    command=pausePlay,
                    bg='#444444'
                 ).place(x=390, y=450)


def criar_prox(raiz):
    global prox_Img
    prox_Img = PhotoImage(file='imagens/botao skip.png')
    return Button(
                    raiz,
                    image=prox_Img,
                    borderwidth=0,
                    bg='#444444'
                 ).place(x=500, y=450)


def criar_back(raiz):
    global back_Img
    back_Img = PhotoImage(file='imagens/botao back.png')
    return Button(
                    raiz,
                    image=back_Img,
                    borderwidth=0,
                    bg='#444444'
                 ).place(x=280, y=450)


def criar_nome(raiz):
    return Label(
                    raiz,
                    text='Só um simples teste',
                    bg='#444444'
                ).configure(font=("Arial", 16)).place(x=310, y=415)


def pausePlay():
    global tocando
    print(tocando)
    if tocando == 'sim':
        pausar()
        tocando = 'nao'

    else:
        despausar()
        tocando = 'sim'
