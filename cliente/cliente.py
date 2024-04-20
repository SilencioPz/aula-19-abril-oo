class Cliente:
    #Array list, para facilitar a visu
    lista_clientes = []

    #Construtor
    def __init__(self, nome, idade, email, endereco):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.endereco = endereco
        self.lista_clientes.append(self)

    #Método de Classe, que fará a impressão das listas
    @classmethod
    def imprimirClientes(cls):
        for cliente in cls.lista_clientes:
            print(f'Cliente: {cliente.nome}, {cliente.idade} anos, {cliente.email}, {cliente.endereco}')