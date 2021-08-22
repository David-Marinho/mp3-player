from tkinter import *
from musicas_Classe import musicas
from os import listdir

arq = listdir('musicas')
raiz = Tk()
raiz.geometry('850x500')

img = PhotoImage(file='imagens/caixas.png')
for i in range(len(arq)):
    if 'mp3' in arq[i].split('.'):
        musica = musicas(raiz, arq[i], img)
        musica.criar_bt()

raiz.mainloop()
