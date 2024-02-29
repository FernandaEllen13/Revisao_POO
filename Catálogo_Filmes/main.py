from classes import Filme
from classes import CatalogoFilmes
from menu import exibir_menu

catalogo = CatalogoFilmes()
print("oi")

while True:
    escolha = exibir_menu()

    if escolha == '1':
        while True:
            titulo = input("Digite o titulo do filme: ")
            ano = input("Digite o ano de seu lançamento: ")
            diretor = input("Digite o nome do diretor(a): ")
            genero = input("Digite o gênero do filme: ")
            duracao = input("Digite a duração em minutos: ")

            filme = Filme(titulo,ano,diretor,genero,duracao)
            catalogo.add_filme(filme)
            continuar = input("Deseja cadastrar outro filme? (s/n) ")
            if continuar.lower()!= 's':
                break
 
    
    elif escolha == '2':
        catalogo.read_filme()


    # elif escolha == '3':
    elif escolha == '3':
        print("Digite o nome do diretor que você deseja pesquisar: ")
        diretor = input()
        catalogo.query_diretor(diretor)

    # elif escolha == '4':


    # elif escolha == '5':


    # elif escolha == '6':


    # elif escolha == '0':


    # else:
    #     print("Opção inválida. Digite novamente.")

