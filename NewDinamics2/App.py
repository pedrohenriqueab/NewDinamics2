from Model.Usuario import Usuario
from Model.Comentario import Comentario
from Database.UsuarioDAO import UsuarioDAO
from Database.ComentarioDAO import ComentarioDAO
'''
Função para exibir o Menu
'''

def exibirMenu():
    print("   === MENU === \n"
        " === DINAMICS ===\n"
        " 1 - Criar usuario\n"
        " 2 - Alterar usuario\n"
        " 3 - Deletar usuario\n"
        " 4 - Listar usuario\n"
        " 5 - Inserir comentário\n"
        " 0 - Sair")

#Função para criar Usuário
def criarUsuario():
    try:
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite seu senha: ")
        data_nasc = input("Digite sua data de nascimento: ")
        profissao = input("Digite seu profissão: ")
        genero = input("Digite seu genero: ")
        cidade = input("Digite seu cidade: ")
        estado = input("Digite seu estado: ")
        pais = input("Digite seu país: ")

        usuario = Usuario(nome, email, senha, data_nasc, profissao, genero, cidade, estado, pais)
        usuarioDAO = UsuarioDAO()
        usuarioDAO.inserir(usuario)

    except:
        print("Oops! Erro encontrado")

#Função para alterar o usuário
def alterarUsuario():
    try:
        id = input("Digite seu ID:")
        novoNome = input("Digite seu nome: ")
        novoEmail = input("Digite seu email: ")
        novoSenha = input("Digite seu senha: ")
        novoData_nasc = input("Digite sua data de nascimento: ")
        novoProfissao = input("Digite seu profissão: ")
        novoGenero = input("Digite seu genero: ")
        novoCidade = input("Digite seu cidade: ")
        novoEstado = input("Digite seu estado: ")
        novoPais = input("Digite seu país: ")
        usuarioDAO = UsuarioDAO
        usuarioDAO.atualizar(id, novoNome, novoEmail, novoSenha, novoData_nasc, novoProfissao, novoGenero, novoCidade, novoEstado, novoPais)

    except:
        print("Oops! Erro encontrado")

#Função para Deletar o usuário
def deletarUsuario():
    try:
        id = input("Digite o seu ID: ")
        usuarioDAO = UsuarioDAO()
        usuarioDAO.deletar(id)

    except:
        print("Oops! Erro encontrado!")

#Função para listar o Usuário
def listarUsuario():
    try:
        usuarioDAO = UsuarioDAO()
        print(usuarioDAO.listar())

    except:
        print("Erro encontrado!")

#Função para inserir Comentário
def inserirComentario():
    try:
        mensagem = input("Digite sua mensagem: ")
        comentario = Comentario(mensagem)
        comentarioDAO = ComentarioDAO()
        comentarioDAO.listar(comentario)

    except:
        print("Erro!")

def main(args = []):

    # Exibição do Menu de Opções.
    exibirMenu()

    continuar = True

    while continuar:
        try:
            # Continuar a execução do programa.
            opcao = int(input("Digite a opção: "))

            if (opcao == 1):
                criarUsuario()

            elif (opcao == 2):
                alterarUsuario()

            elif (opcao == 3):
                deletarUsuario()

            elif (opcao == 4):
                listarUsuario()

            elif (opcao == 5):
                inserirComentario()

            elif (opcao == 0):
                continuar = False
            else:
                print("Ops! Opção inválida!")

        except ValueError:
            print("Ops! Digite um valor válido")

if (__name__ == "__main__"):
    main()
