#Importação para tratar dos métodos abstratos
from abc import ABC, abstractmethod

class ItemCatalogo(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    #Método que pode ser usado por itemCatalogo
    @abstractmethod
    #Cada desconto pode ser feito individualmente
    def aplicarDesconto(self):
        pass