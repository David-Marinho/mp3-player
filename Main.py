from tkinter import *
from musicas_Classe import bt_musicas
from os import listdir
from classe_menu import menu
from win32api import GetSystemMetrics

largura = GetSystemMetrics(0)
altura = GetSystemMetrics(1)
arq = listdir('musicas')
raiz = Tk()
raiz.geometry(f'{largura}x{altura}')

img = PhotoImage(file='imagens/caixas.png')
for i in range(len(arq)):
    if 'mp3' in arq[i].split('.'):
        musica = bt_musicas(raiz, arq[i], img)
        musica.criar_bt()

menu = menu(raiz)
menu.criar_menu()

raiz.mainloop()
