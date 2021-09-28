from classse_janela import janela
from os import listdir
from classe_menu import menu

arq = listdir('musicas')
raiz = janela()
tela = raiz.criar()

tela.mainloop()

menu = menu(tela)
menu.criar_menu(raiz.tamY, raiz.tamX)

"""img = PhotoImage(file='imagens/caixas.png')
for i in range(len(arq)):
    if 'mp3' in arq[i].split('.'):
        musica = bt_musicas(raiz, arq[i], img)
        musica.criar_bt()

menu = menu(raiz)
menu.criar_menu(altura, largura)

raiz.mainloop()"""
