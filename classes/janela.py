from win32api import GetSystemMetrics
from tkinter import Tk


class janela():
    def __init__(self):
        self.tamX = GetSystemMetrics(0)
        self.tamY = GetSystemMetrics(1)

    def criar(self):
        tela = Tk()
        tela.geometry(f'{self.tamX}x{self.tamY}')
        tela.config(bg='#1C364F')
        tela.state('zoomed')
        return tela