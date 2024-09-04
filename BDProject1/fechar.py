from tkinter import *
from tkinter import ttk, messagebox


class SistemaUsuarios:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Sistema de Usuários")

        # Criação da janela principal
        self.janela_principal = Frame(master)
        self.janela_principal.pack(padx=20, pady=20)

        # Botões na janela principal
        self.botao_usuario = Button(self.janela_principal, text="Usuário", command=self.janela_usuario)
        self.botao_usuario.pack(side=LEFT, padx=10)

        self.botao_cidades = Button(self.janela_principal, text="Cidades", command=self.janela_cidades)
        self.botao_cidades.pack(side=LEFT, padx=10)

        self.botao_clientes = Button(self.janela_principal, text="Clientes", command=self.janela_clientes)
        self.botao_clientes.pack(side=LEFT, padx=10)

        self.botao_fechar = Button(self.janela_principal, text="Fechar", command=self.master.quit)
        self.botao_fechar.pack(side=LEFT, padx=10)

    def janela_usuario(self):
        # Criação da janela de Usuário
        self.janela_usuario = Toplevel(self.master)
        self.janela_usuario.title("Cadastro de Usuário")

        # Criação da janela de Usuário
        self.janela_usuario_frame = Frame(self.janela_usuario)
        self.janela_usuario_frame.pack(padx=20, pady=20)

        # Título
        self.titulo = Label(self.janela_usuario_frame, text="Informe os dados:")
        self.titulo.pack(pady=10)

        # Campos de entrada
        self.campos_frame = Frame(self.janela_usuario_frame)
        self.campos_frame.pack(anchor=W)

        self.idusuario_label = Label(self.campos_frame, text="IdUsuario:")
        self.idusuario_label.pack(side=LEFT)
        self.idusuario_entry = Entry(self.campos_frame)
        self.idusuario_entry.pack(side=LEFT, padx=5)

        self.botao_buscar = Button(self.campos_frame, text="Buscar", command=self.buscar_usuario)
        self.botao_buscar.pack(side=LEFT, padx=5)

        self.nome_label = Label(self.janela_usuario_frame, text="Nome:")
        self.nome_label.pack(anchor=W)
        self.nome_entry = Entry(self.janela_usuario_frame)
        self.nome_entry.pack(anchor=W)

        self.telefone_label = Label(self.janela_usuario_frame, text="Telefone:")
        self.telefone_label.pack(anchor=W)
        self.telefone_entry = Entry(self.janela_usuario_frame)
        self.telefone_entry.pack(anchor=W)

        self.email_label = Label(self.janela_usuario_frame, text="Email:")
        self.email_label.pack(anchor=W)
        self.email_entry = Entry(self.janela_usuario_frame)
        self.email_entry.pack(anchor=W)

        self.usuario_label = Label(self.janela_usuario_frame, text="Usuário:")
        self.usuario_label.pack(anchor=W)
        self.usuario_entry = Entry(self.janela_usuario_frame)
        self.usuario_entry.pack(anchor=W)

        self.senha_label = Label(self.janela_usuario_frame, text="Senha:")
        self.senha_label.pack(anchor=W)
        self.senha_entry = Entry(self.janela_usuario_frame)
        self.senha_entry.pack(anchor=W)

        # Botões de ação
        self.botoes_frame = Frame(self.janela_usuario_frame)
        self.botoes_frame.pack(pady=10)

        self.botao_inserir = Button(self.botoes_frame, text="Inserir", command=self.inserir_usuario)
        self.botao_inserir.pack(side=LEFT, padx=5)

        self.botao_alterar = Button(self.botoes_frame, text="Alterar", command=self.alterar_usuario)
        self.botao_alterar.pack(side=LEFT, padx=5)

        self.botao_excluir = Button(self.botoes_frame, text="Excluir", command=self.excluir_usuario)
        self.botao_excluir.pack(side=LEFT, padx=5)

    def janela_cidades(self):
        # Criação da janela de Cidades
        self.janela_cidades = Toplevel(self.master)
        self.janela_cidades.title("Cadastro de Cidades")
        # Adicione os widgets e funcionalidades para a janela de Cidades

    def janela_clientes(self):
        # Criação da janela de Clientes
        self.janela_clientes = Toplevel(self.master)
        self.janela_clientes.title("Cadastro de Clientes")
        # Adicione os widgets e funcionalidades para a janela de Clientes

    def buscar_usuario(self):
        # Função para buscar um usuário
        idusuario = self.idusuario_entry.get()

        # Aqui você pode adicionar a lógica para buscar o usuário no banco de dados ou em uma lista

        # Preencher os campos com os dados do usuário encontrado
        self.nome_entry.insert(0, "Nome do Usuário")
        self.telefone_entry.insert(0, "Telefone do Usuário")
        self.email_entry.insert(0, "Email do Usuário")
        self.usuario_entry.insert(0, "Usuario do Usuário")
        self.senha_entry.insert(0, "Senha do Usuário")

    def inserir_usuario(self):
        # Função para inserir um usuário
        idusuario = self.idusuario_entry.get()
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        # Aqui você pode adicionar a lógica para inserir o usuário no banco de dados ou em uma lista

        messagebox.showinfo("Inserir Usuário", f"Usuário {nome} inserido com sucesso!")

    def alterar_usuario(self):
        # Função para alterar um usuário
        idusuario = self.idusuario_entry.get()
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        email = self.email_entry.get()
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        # Aqui você pode adicionar a lógica para alterar o usuário no banco de dados ou em uma lista

        messagebox.showinfo("Alterar Usuário", f"Usuário {nome} alterado com sucesso!")

    def excluir_usuario(self):
        # Função para excluir um usuário
        idusuario = self.idusuario_entry.get()
        nome = self.nome_entry.get()

        # Aqui você pode adicionar a lógica para excluir o usuário no banco de dados ou em uma lista

        messagebox.showinfo("Excluir Usuário", f"Usuário {nome} excluído com sucesso!")


if __name__ == "__main__":
    root = Tk()
    app = SistemaUsuarios(root)
    root.mainloop()