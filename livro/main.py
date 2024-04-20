# Importações dos arquivos livro e menu
from livro import Livro
from menu import main

livro1 = Livro('O Guia do Mochileiro das Galáxias', 'Comédia', False)
livro2 = Livro('À Espera de Um Milagre', 'Drama', True)
livro3 = Livro('Começando a programar em Python Para leigos', 'Programação', False)
livro4 = Livro('1984', 'Ficção', True)
livro5 = Livro('O Sol é Para Todos', 'Ficção', False)
livro6 = Livro('O Senhor dos Anéis', 'Aventura', True)
livro7 = Livro('Cem Anos de Solidão', 'Realista', False)

#"Puxa" as funções presentes no arquivo menu
if __name__ == '__main__':
    main()