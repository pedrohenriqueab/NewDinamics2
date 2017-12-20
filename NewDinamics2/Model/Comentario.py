import datetime
'''
    Criação da classe Comentário
'''
class Comentario():
    def __init__(self, mensagem):
        self.mensagem = mensagem
        self.dataHora = datetime.datetime.now()
