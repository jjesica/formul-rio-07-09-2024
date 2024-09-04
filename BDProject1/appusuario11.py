from tkinter import *
from tkinter import messagebox

class Usuario:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.janela = Frame(master)
        self.janela.pack(padx=10, pady=10)

        self.msg = Label(self.janela, text="Informe os dados:")
        self.msg["font"] = self.fontePadrao
        self.msg.pack()

        # Frame para ID do Usuário
        self.janela2 = Frame(self.janela)
        self.janela2.pack(pady=5)

        self.idLabel = Label(self.janela2, text="IdUsuario:", font=self.fontePadrao, width=10)
        self.idLabel.pack(side=LEFT)
        self.id_entry = Entry(self.janela2, width=12, font=self.fontePadrao)
        self.id_entry.pack(side=LEFT)

        self.bus = Button(self.janela2, text="Buscar", font=("Calibri", "12"), width=10, command=self.buscarUsuario)
        self.bus.pack(side=RIGHT)

        # Frame para Nome
        self.janela3 = Frame(self.janela)
        self.janela3.pack(pady=5)

        self.nomeLabel = Label(self.janela3, text="Nome:", font=self.fontePadrao, width=10)
        self.nomeLabel.pack(side=LEFT)
        self.nome_entry = Entry(self.janela3, width=25, font=self.fontePadrao)
        self.nome_entry.pack(side=LEFT)

        # Frame para Telefone
        self.janela4 = Frame(self.janela)
        self.janela4.pack(pady=5)

        self.telLabel = Label(self.janela4, text="Telefone:", font=self.fontePadrao, width=10)
        self.telLabel.pack(side=LEFT)
        self.tel_entry = Entry(self.janela4, width=25, font=self.fontePadrao)
        self.tel_entry.pack(side=LEFT)

        # Frame para E-mail
        self.janela5 = Frame(self.janela)
        self.janela5.pack(pady=5)

        self.emailLabel = Label(self.janela5, text="E-mail:", font=self.fontePadrao, width=10)
        self.emailLabel.pack(side=LEFT)
        self.email_entry = Entry(self.janela5, width=25, font=self.fontePadrao)
        self.email_entry.pack(side=LEFT)

        # Frame para Usuário
        self.janela6 = Frame(self.janela)
        self.janela6.pack(pady=5)

        self.usuLabel = Label(self.janela6, text="Usuário:", font=self.fontePadrao, width=10)
        self.usuLabel.pack(side=LEFT)
        self.usu_entry = Entry(self.janela6, width=25, font=self.fontePadrao)
        self.usu_entry.pack(side=LEFT)

        # Frame para Senha
        self.janela7 = Frame(self.janela)
        self.janela7.pack(pady=5)

        self.senhaLabel = Label(self.janela7, text="Senha:", font=self.fontePadrao, width=10)
        self.senhaLabel.pack(side=LEFT)
        self.senha_entry = Entry(self.janela7, width=25, font=self.fontePadrao, show="*")
        self.senha_entry.pack(side=LEFT)

        # Botões de Ação
        self.janela8 = Frame(self.janela)
        self.janela8.pack(pady=5)

        self.usua = Button(self.janela8, text="Inserir", font=("Calibri", "12"), width=14, command=self.inserirUsuario)
        self.usua.pack(side=LEFT)

        self.cidade = Button(self.janela8, text="Alterar", font=("Calibri", "12"), width=14, command=self.alterarUsuario)
        self.cidade.pack(side=LEFT)

        self.clie = Button(self.janela8, text="Excluir", font=("Calibri", "12"), width=14, command=self.excluirUsuario)
        self.clie.pack(side=LEFT)

    def buscarUsuario(self):
        idusuario = self.id_entry.get()

    def inserirUsuario(self):
        nome = self.nome_entry.get()
        tel = self.tel_entry.get()
        email = self.email_entry.get()
        usuario = self.usu_entry.get()
        senha = self.senha_entry.get()

    def alterarUsuario(self):
        idusuario = self.id_entry.get()
        nome = self.nome_entry.get()
        tel = self.tel_entry.get()
        email = self.email_entry.get()
        usuario = self.usu_entry.get()
        senha = self.senha_entry.get()


    def excluirUsuario(self):
        idusuario = self.id_entry.get()


if __name__ == "__main__":
    root = Tk()
    root.title("Cadastro de Usuários")
    root.state("zoomed")
    app = Usuario(root)
    root.mainloop()