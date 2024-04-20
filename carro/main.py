# "Puxando" dados dos dois arquivos
from carro import Carro
from conversao import __str__

#Instâncias
carro1 = Carro('Fusca', 'Azul', 1968)
carro2 = Carro('Gol', 'Branca', 1995)
carro3 = Carro('Uno', 'Vermelha', 2000)
carro4 = Carro('Golf GTI', 'Preta', 2010)
carro5 = Carro('Onix', 'Prata', 2020)

#Prints
Carro.imprimirTodosCarros()