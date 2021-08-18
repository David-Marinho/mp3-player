import tkinter as tk


class mp3:
    def __init__(self, root: tk.Tk):
        self.root = root
        """self.music_Btn = music_Btn
        self.menu_Btn = menu_Btn
        self.menu_Label = menu_Label"""

    def criar_Menu(self):
        global menu_Img
        menu_Img = tk.PhotoImage(file='imagens/barra.png')
        menu = tk.Label(self.root, image=menu_Img, borderwidth=0)
        menu.place(x=0, y=410)
        self.btn_PausePlay()


    def algo(self):
        pass

    def btn_PausePlay(self):
        global btn_Img
        btn_Img = tk.PhotoImage(file='imagens/botao pause.png')
        btn = tk.Button(self.root, image=btn_Img, borderwidth=0, command=self.algo, bg='#444444')
        btn.place(x=390, y=450)
        self.criar_prox()


    def criar_prox(self):
        global prox_Img
        prox_Img = tk.PhotoImage(file='imagens/botao skip.png')
        btn = tk.Button(self.root, image=prox_Img, borderwidth=0, command=self.algo, bg='#444444')
        btn.place(x=500, y=450)
        self.criar_back()

    def criar_back(self):
        global back_Img
        back_Img = tk.PhotoImage(file='imagens/botao back.png')
        btn = tk.Button(self.root, image=back_Img, borderwidth=0, command=self.algo, bg='#444444')
        btn.place(x=280, y=450)
        self.criar_nome()



    def criar_nome(self):
        lb = tk.Label(self.root, text='Só um simples teste', bg='#444444')
        lb.configure(font=("Arial", 16))
        lb.place(x=310, y=415)

        """janela = Tk()
        janela.geometry("850x500")

        barra_image = PhotoImage(file='imagens/barra.png')
        barra_Lb = Label(width=850, height=97, image=barra_image)
        barra_Lb.place(x=0, y=402)

        pause_logo = PhotoImage(file='imagens/botao pause.png')
        pausePlay = Button(janela,  image=pause_logo, borderwidth=0, bg='#444444', )
        pausePlay.place(x=400, y=450)

        janela.mainloop()

    @staticmethod
    def add_btn(nome, mestre):
        print(nome)
        bt = Button(mestre, text=nome)
        bt.grid(sticky='w')"""
