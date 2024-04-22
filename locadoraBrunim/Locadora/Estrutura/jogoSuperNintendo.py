from Locadora.Estrutura.itemCatalogo import ItemCatalogo

class JogoSuperNintendo(ItemCatalogo):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def aplicarDesconto(self):
        self._preco -= (self._preco * 0.08)