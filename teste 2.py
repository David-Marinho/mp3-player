from tkinter import *

jan = Tk()
jan.geometry("500x500")
jan.configure(background="#f0f0f0")

pause_logo = PhotoImage(file = "rosto0.png")
label = Label(jan, image = pause_logo)
label.place(x=100 , y=10)


def crt():
   pause_logo['file'] = "rosto1.png"


crt = Button(jan, text="TROCAR ROSTO", font=("Centurty Gothic",10), command=crt)
crt.place(x=5, y=10)

jan.mainloop()