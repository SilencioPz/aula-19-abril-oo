# Importando o arquivo cliente.py
from cliente import Cliente

#Instâncias a serem impressas
cliente1 = Cliente('Joaozim', 23, 'joaozim@gmail.com', 'Rua das Flores número 123')
cliente2 = Cliente('Carolzim', 17, 'carolzim@gmail.com', 'Avenida das Árvores número 456')
cliente3 = Cliente('Rauzim', 25, 'rauzim@gmail.com', 'Praça dos Pássaros número 789')

#Impressão com base no método de classe
Cliente.imprimirClientes()