from func import *
from mp3_Classe import mp3
from os import listdir
from func import musicas

root = criar_Janela()
mp3 = mp3(root)
mp3.criar_Menu()
mp3.criar_musica(musicas(listdir('musicas')))


root.mainloop()