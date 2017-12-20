'''
    Criação da classe Usuario
'''
class Usuario():
    def __init__(self, nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais, id=None):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.data_nasc = data_nasc
        self.profissao = profissao
        self.genero = genero
        self.cidade = cidade
        self.estado = estado
        self.pais = pais
