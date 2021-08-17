"""from os import listdir

for i in listdir('musicas'):
    if 'mp3' in i.split('.'):
        print('ok')"""
from func import *
from mp3_Classe import mp3
root = criar_Janela()
mp3 = mp3(root)
mp3.criar_Menu()


root.mainloop()
