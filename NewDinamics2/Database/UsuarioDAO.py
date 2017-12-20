import sqlite3
from Model.Usuario import Usuario

class UsuarioDAO():
    #Função para inserir Usuário
    def inserir(self, usuario):
        try:
            conn = sqlite3.connect('dinamics.db')
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO tb_Usuario (nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais)
                VALUES (?,?,?,?,?,?,?,?,?)""",
                (usuario.nome, usuario.email, usuario.senha,  usuario.data_nasc,  usuario.profissao,  usuario.genero,  usuario.cidade,  usuario.estado,  usuario.pais))

            conn.commit()

        except Exception as err:
            print(err)
            print("Ocorreu um erro!")

        finally:
            cursor.close()
            conn.close()

    #Função para alterar Usuário
    def atualizar(self, id, novoNome, novoEmail, novoSenha, novoData_nasc, novoProfissao, novoGenero, novoCidade, novoEstado, novoPais):
        try:
            conn = sqlite3.connect('dinamics')
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE tb_Usuario
                SET nome = ?, email = ?, senha = ?, data_nasc = ?, profissao = ?, genero = ?, cidade = ?, estado = ?, pais = ?
                WHERE id = ?""", (id, novoNome, novoEmail, novoSenha, novoData_nasc, novoProfissao, novoGenero, novoCidade, novoEstado, novoPais))

            conn.commit()

        except Exception as err:
            print(err)
            print("Ocorreu um erro!")

        finally:
            cursor.close()
            conn.close()

    #Função para deletar Usuário
    def deletar(self, id):
        try:
            conn = sqlite3.connect('dinamics')
            cursor = conn.cursor()

            cursor.execute("""
            DELETE FROM tb_Usuario WHERE id = ?
            """, (id))

            conn.commit()

        except Exception as err:
            print(err)
            print("Ocorreu um erro!")

        finally:
            cursor.close()
            conn.close()

    #Função para listar Usuários
    def listar(self):
        usuarios = []
        try:
            conn = sqlite3.connect('dinamics')
            cursor = conn.cursor()

            cursor.execute("""
            SELECT * FROM tb_Usuario
                """)


            for linha in cursor.fetchall():
                id = linha[0]
                nome = linha[1]
                email = linha[2]
                senha = linha[3]
                data_nasc = linha[4]
                profissao = linha[5]
                genero = linha[6]
                cidade = linha[7]
                estado = linha[8]
                pais = linha[9]

                usuario = Usuario(nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais, id)

                usuarios.append(usuario)

        except Exception as err:
            print(err)
            print("Ocorreu um erro!")

        finally:
            cursor.close()
            conn.close()

            return usuarios
