from pygame import mixer
from os import listdir

lista = list()
mixer.init()
cont = 1


for i in listdir('musicas'):
    print(f'{cont} = {i}')
    lista.append(i)
    cont += 1

musica = int(input('digite o numero da musica que voce quer escutar: ')) - 1
print(f'tocando: {lista[musica]}')
mixer.music.load(f'musicas/{lista[musica]}')
mixer.music.play()
while True:
    escolha = str(input('digite: \n\nstop \nnext \npause \ndespause \nsair \n\noque voce quer fazer? '))

    if escolha == 'stop':
        mixer.music.stop()

    elif escolha == 'next':
        mixer.music.stop()
        musica +=1
        mixer.music.load(f'musicas/{lista[musica]}')
        mixer.music.play()
        print(f'tocando: {lista[musica]}')
    
    elif escolha == 'pause':
        mixer.music.pause()
    
    elif escolha == 'despause':
        mixer.music.unpause()
    
    elif escolha == 'sair':
        mixer.music.stop()
        break

    else:
        print('comando nao reconhecido. Por favor, tente novamente \n')
    
    escolha = None