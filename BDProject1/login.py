from tkinter import *

from select import select


class login:
    def __init__(self, master):
        self.fnt = ("Verdana","8")

        self.janela = Frame(master)
        self.janela("padx") = 20
        self.janela("pady") = 5
        self.janela.pack()

        self.wdgt1 = Frame(master)
        self.wdgt1("padx") = 20
        self.wdgt1("pady") = 5
        self.wdgt1.pack()

        self.wdgt2 = Frame(master)
        self.wdgt2("padx") = 20
        self.wdgt2("pady") = 5
        self.wdgt2.pack()

        self.wdgt3 = Frame(master)
        self.wdgt3("padx") = 20
        self.wdgt3("pady") = 5
        self.wdgt3.pack()

        self.img = PhotoImage(file="img/imagens.png")
        self.lblimg = Label(self.janela. image=self.img)
        self.lblimg.pack()

        self.lblusuario = Label(self.wdgt1, text="Usuario:", font=self.fnt, width=10)
        self.lblusuario.pack(side=LEFT)
        self.txtusuario = Entry(self.wdgt1)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fnt
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.wdgt1, text="Senha:", font=self.fnt, width=10)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha = Entry(self.wdgt1)
        self.txtsenha["width"] = 25
        self.txtsenha["font"] = self.fnt
        self.txtsenha.pack(side=LEFT)



