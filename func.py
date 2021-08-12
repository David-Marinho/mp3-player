from pygame import mixer
from tkinter import *




def pause_play():
    global tocando
    global pausePlay
    if tocando:
        mixer.music.pause()
        tocando = False
        pause_logo = PhotoImage(file='outline_play_arrow_black_24dp.png')


    else:
        mixer.music.unpause()
        tocando = True
        pause_logo = PhotoImage(file='outline_pause_black_24dp.png')

    pausePlay.config(image=pause_logo)