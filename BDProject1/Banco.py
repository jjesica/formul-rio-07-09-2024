import sqlite3

class Banco():
    def init(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""create table if not exists tbl_usuarios(
        idusuario integer primary key autoincrement,
        nome text,
        telefone text,
        email text,
        usuario text,
        senha text)""")
        self.conexao.commit()
        c.close()