class Carro:
    #Array list, pra facilitar a visu
    listaCarros = []

    #Construtor
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.listaCarros.append(self)

    #Método de classe, que fará as impressões
    @classmethod
    def imprimirTodosCarros(cls):
        for carro in cls.listaCarros:
            print(carro)