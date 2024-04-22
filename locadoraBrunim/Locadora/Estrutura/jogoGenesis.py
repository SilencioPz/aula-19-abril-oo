from Locadora.Estrutura.itemCatalogo import ItemCatalogo

class JogoGenesis(ItemCatalogo):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao 

    def aplicarDesconto(self):
        self._preco -= (self._preco * 0.04)