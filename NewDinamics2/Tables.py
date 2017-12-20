import sqlite3

#Funçao para criar tabelas
def criarTabelas():
    try:
        conn = sqlite3.connect('dinamics.db')
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE tb_Usuario (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(50) NOT NULL,
                email VARCHAR(50) NOT NULL,
                senha VARCHAR(10) NOT NULL,
                data_nasc DATE,
                profissao VARCHAR(20),
                genero VARCHAR(10),
                cidade VARCHAR(20),
                estado VARCHAR(20),
                pais VARCHAR(20));
        """)

        print("Tabela tb_Usuario criada com sucesso!")

        cursor.execute("""
        CREATE TABLE tb_Comentario (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                mensagem VARCHAR(150),
                dataHora DATETIME);
        """)

        print("Tabela tb_Comentario criada com sucesso!")

    except Exception as err:
        print(err)

criarTabelas()
