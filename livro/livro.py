class Livro:
    #Array list, pra facilitar a visu
    listaLivros = []

    #Construtor
    def __init__(self, nome, categoria, ativo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.listaLivros.append(self)

    #Método de classe para Inserção de novos livros
    @classmethod
    def cadastrarLivro(cls, nome, categoria, ativo):
        cls(nome, categoria, ativo)

    #Método de classe para Leitura dos livros
    @classmethod
    def listarLivros(cls):
        for livro in cls.listaLivros:
            ativo = 'ativado' if livro.ativo else 'desativado'
            print(f'- {livro.nome.ljust(35)} | {livro.categoria.ljust(35)} | {ativo}')

    #Método de classe para o Atualizar Livros
    @classmethod
    def alterarLivro(cls, nome):
        for livro in cls.listaLivros:
            if livro.nome == nome:
                livro.ativo = not livro.ativo
                return True
        return False

    #Método de classe para Remover livros cadastrados
    @classmethod
    def removerLivro(cls, nome):
        for livro in cls.listaLivros:
            if livro.nome == nome:
                cls.listaLivros.remove(livro)
                return True
        return False