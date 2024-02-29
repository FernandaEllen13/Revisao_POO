class Filme:
    def __init__(self, titulo, ano, diretor, genero, duracao):
        self.titulo = titulo
        self.ano = ano
        self.diretor = diretor
        self.genero = genero
        self.duracao = duracao


class CatalogoFilmes:
    def __init__(self):
        self.filmes =  []

    def add_filme(self,filme):
        self.filmes.append(filme)

    def read_filme(self):
        print("-" * 30)
        print("Filmes Cadastrados:")
        for i, filme in enumerate(self.filmes, start=1):
            
            print(f"Filme {i}:")
            print(f"Título: {filme.titulo}")
            print(f"Ano de Lançamento: {filme.ano}")
            print(f"Diretor: {filme.diretor}")
            print(f"Gênero: {filme.genero}")
            print(f"Duração: {filme.duracao} minutos")
            print("-" * 30)

    def query_ano(self,ano):
        for filme in self.filmes:
            if filme.ano == ano:
                print(filme.nome,filme.ano)

    def query_genero(self,genero):
        for filme in self.filmes:
            if filme.genero == genero:
                print(filme.titulo,filme.ano)


    def query_diretor(self,diretor):
        for filme in self.filmes:
            if filme.diretor == diretor:
                print(filme.titulo,filme.ano)

