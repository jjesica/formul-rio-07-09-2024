from tkinter import *

class Tabela:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial","12")
        self.janela = Frame(master)
        self.janela.pack()
        self.msg = Label(self.janela, text="Sistema de cadastro")
        self.msg["font"] = self.fontePadrao
        self.msg.pack()

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.usua = Button(self.janela2)
        self.usua["text"] = "Usuário"
        self.usua["font"] = self.fontePadrao
        self.usua["width"] = 14
        self.usua["command"] = self.janela2
        self.usua.pack(side=LEFT)

        self.cidade = Button(self.janela2)
        self.cidade["text"] = "Cidades"
        self.cidade["font"] = self.fontePadrao
        self.cidade["width"] = 14
        self.cidade["command"] = self.janela2
        self.cidade.pack(side=LEFT)

        self.clie = Button(self.janela2)
        self.clie["text"] = "Clientes"
        self.clie["font"] = self.fontePadrao
        self.clie["width"] = 14
        self.clie["command"] = self.janela2
        self.clie.pack(side=LEFT)

        self.fechar = Button(self.janela2)
        self.fechar["text"] = "Fechar"
        self.fechar["font"] = ("Calibri", "12")
        self.fechar["width"] = 14
        self.fechar["command"] = self.janela2
        self.fechar.pack(side=LEFT)

root = Tk()
Tabela(root)
root.state("zoomed")
root.mainloop()