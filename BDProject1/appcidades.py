from tkinter import *

class Cidade:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial","10")
        self.janela = Frame(master)
        self.janela.pack()
        self.msg = Label(self.janela, text="Informe os dados:")
        self.msg["font"] = self.fontePadrao
        self.msg.pack()

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()


        self.idLabel = Label(self.janela2, text="Cidade:", font=self.fontePadrao, width= 10)
        self.idLabel.pack(side=LEFT)
        self.id = Entry(self.janela2)
        self.id["width"] = 12
        self.id["font"] = self.fontePadrao
        self.id.pack(side=LEFT)

        self.idLabel = Label(self.janela3, text="Estado:", font=self.fontePadrao, width= 10)
        self.idLabel.pack(side=LEFT)
        self.id = Entry(self.janela3)
        self.id["width"] = 25
        self.id["font"] = self.fontePadrao
        self.id.pack(side=LEFT)

        self.telLabel = Label(self.janela4, text="Cep:", font=self.fontePadrao, width= 10)
        self.telLabel.pack(side=LEFT)
        self.tel = Entry(self.janela4)
        self.tel["width"] = 25
        self.tel["font"] = self.fontePadrao
        self.tel.pack(side=LEFT)




root = Tk()
Cidade(root)
root.state("zoomed")
root.mainloop()