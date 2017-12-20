import sqlite3
from Model.Comentario import Comentario

'''
Criação da classe ComentarioDAO
'''

class ComentarioDAO():
#Função para listar Mensagens
    def listar(self, comentario):
        try:
            conn = sqlite3.connect('dinamics.db')
            cursor = conn.cursor()
            cursor.execute(""" INSERT INTO tb_Comentario (mensagem, dataHora)
            VALUES (?,?)""", (comentario.mensagem, comentario.dataHora))
            conn.commit()

        except Exception as err:
            print(err)
            print("Ocorreu um erro!")

        finally:
            cursor.close()
            conn.close()




