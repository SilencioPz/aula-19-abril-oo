from Locadora.avaliacaoJogo import AvaliacaoJogo
from Locadora.Estrutura.itemCatalogo import ItemCatalogo

class Jogo:
    jogos = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._catalogo = []
        Jogo.jogos.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listarJogos(cls):
        print(f'{"Nome do jogo".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} |{"Status"}')
        for jogo in cls.jogos:
            print(f'{jogo._nome.ljust(25)} | {jogo._categoria.ljust(25)} | {str(jogo.media_avaliacoes).ljust(25)} |{jogo.ativo}')

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    def alternarEstado(self):
        self._ativo = not self._ativo

    def receberAvaliacao(self, jogador, nota):
        if 0 < nota <= 5: 
            avaliacao = AvaliacaoJogo(jogador, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        somaDasNotas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidadeDeNotas = len(self._avaliacao)
        media = round(somaDasNotas / quantidadeDeNotas, 1)
        return media

    def adicionarNoCatalogo(self,item):
        if isinstance(item,ItemCatalogo):
            self._catalogo.append(item)
    
    @property
    def exibirCatalogo(self):
        print(f'Catalogo da Locadora {self._nome}\n')
        for i,item in enumerate(self._catalogo,start=1):
            if hasattr(item,'descricao'):
                mensagemItem = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagemItem)
            else:
                mensagemItem = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                print(mensagemItem)