from tkinter import*
from tkinter import ttk

from select import select

from appusuario11 import Usuario
from usuario import *

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Formulário de Usuários")
        
        self.janela1 = Frame(master)
        self.janela1.pack(padx=10, pady=10)

        self.msg1 = Label(self.janela1, text="Informe os dados:")
        self.msg1["font"] = ("verdana", "14", "bold")
        self.msg1.pack()

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idusuario_label = Label(self.janela2, text="id usuario:")
        self.idusuario_label.pack(side="left")
        self.idusuario = Entry(self.janela2, width=20)
        self.idusuario.pack(side="left")

        self.busca = Button(self.janela2)
        self.busca["text"] = "Buscar"
        self.busca["command"] = self.buscarusuario

        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nome_label = Label(self.janela3, text="Nome:")
        self.nome_label.pack(side="left")
        self.nome = Entry(self.janela3, width=20)
        self.nome.pack(side="left")

        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.telefone_label = Label(self.janela4, text="Telefone:")
        self.telefone_label.pack(side="left")
        self.telefone = Entry(self.janela4, width=20)
        self.telefone.pack(side="left")

        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        self.email_label = Label(self.janela5, text="Email:")
        self.email_label.pack(side="left")
        self.email = Entry(self.janela5, width=20)
        self.email.pack(side="left")

        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.usuario_label = Label(self.janela6, text="Usuário:")
        self.usuario_label.pack(side="left")
        self.usuario = Entry(self.janela6, width=20)
        self.usuario.pack(side="left")

        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack()

        self.senha_label = Label(self.janela7, text="Senha:")
        self.senha_label.pack(side="left")
        self.senha = Entry(self.janela7, width=20)
        self.senha.pack(side="left")

        self.janela8 = Frame(master)
        self.janela8["padx"] = 20
        self.janela8.pack()

        self.autentic = Label(self.janela8, text="")
        self.autentic["font"] = ("Verdana", "10", "italic", "bold")
        self.autentic.pack()

        self.janela9 = Frame(master)
        self.janela9["padx"] = 20
        self.janela9.pack()

        self.botao = Button(self.janela9, width=10, text="Inserir", command=self.inserirusuario)
        self.botao.pack(side="left")

        self.botao2 = Button(self.janela9, width=10, text="Alterar", command=self.alterarusuario)
        self.botao2.pack(side="left")

        self.botao3 = Button(self.janela9, width=10, text="Excluir", command=self.excluirusuario)
        self.botao3.pack(side="left")

        self.janela10 = Frame(master)
        self.janela10"padx"] = 20
        self.janela10.pack()

        self.tree = ttk.Treeview(self.janela10, columns=("ID","Nome","Telefone","E-mail","Usuario")show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Telefone", text="Telefone")
        self.tree.heading("E-mail", text="E-mail")
        self.tree.heading("Usuario", text="Usuario")
        self.tree.pack()
        self.tree.bind("<<TreeviewSelect", self.selecionausuario)

        self.atualizarTabela()

    def selecionarusuario(self, event):

            seliciona_item = self.tree.selection()
            if seliciona_item:
                item = seliciona_item[0]
                valeus = self.tree.item(item, 'valeus')
                self.idusuario.delete(0 ,END)
                self.idusuario.insert(INSERT, values[0])
                self.nome.delete(0, END)
                self.nome.insert(INSERT, values[2])
                self.telefone.delete(0 ,END)
                self.telefone.insert(INSERT, values[2])
                self.email.delete(0 ,END)
                self.email.insert(INSERT, values[3])
                self.usuario.delete(0 ,END)
                self.usuario.insert(INSERT, values[4])
                self.senha.delete(0 ,END)
                self.senha.insert(INSERT, values[5])

    def atualizarTabela (self):
        user = Usuarios()
        usuarios = user.selectAllUser()
        self.tree.delete(*self.tree.get_children())
        for u in usuarios:
            self.tree.insert(**, "end", values=(u[0]))

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.idusuario.get()
        self.autentic["text"] = user.selectUser(idusuario)
        self.idusuario.delete(0, END)
        self.idusuario.insert(INSERT, user.idusuario)
        self.nome.delete(0, END)
        self.nome.insert(INSERT, user.nome)
        self.telefone.delete(0, END)
        self.telefone.insert(INSERT, user.telefone)
        self.email.delete(0, END)
        self.email.insert(INSERT, user.email)
        self.usuario.delete(0, END)
        self.usuario.insert(INSERT, user.usuario)
        self.senha.delete(0, END)
        self.senha.insert(INSERT, user.senha)

        self.atualizarTabela()()

    def inserirusuario(self):
        user = usuarios()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        self.autentic["text"] = user.insertUser
        self.limparCampos()
        self.atualizarTabela()

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        user.nome = self.nome.get()
        user.telefone = self.telefone.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        self.autentic["text"] = user.insertUser
        self.limparCampos()
        self.atualizarTabela()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.idusuario.get()
        self.autentic["text"] = user.deleteUser()
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos
        self.idusuario.delete(0, END)
        self.nome.delete(0, END)
        self.telefone.delete(0, END)
        self.email.delete(0, END)
        self.usuario.delete(0, END)
        self.senha.delete(0, END)
        self.tree.delete(*self.tree.get_children())

if __name__ == *__main__":
    root = TK()
    Application(root)
    root.mainloop()