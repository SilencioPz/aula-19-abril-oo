#Import pra limpar tela e referência do arquivo livro classe Livro
import os
from livro import Livro

#Cada telinha do programa logo abaixo
def exibirNomePrograma():
    print('BIBLIOTECA DO BRUNIM 1.0')

def exibirOpcoes():
    print('1. Cadastrar livro')
    print('2. Listar livros')
    print('3. Alternar estado de um livro')
    print('4. Remover livro')
    print('5. Sair\n')

def finalizar():
    print('Falou, um abraço! :D')

def voltarMenuPrincipal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcaoInvalida():
    print('Opção inválida!\n')
    voltarMenuPrincipal()

#Frescurites pra embelezar a tela
def exibirSubtitulo(texto):
    os.system('cls')
    #Cria uma linha de asteriscos, baseando-se no múmero de caracteres de um texto. Exemplo: brunim = *****
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

#Aqui são tratadas as 5 escolhas do programa
def escolherOpcao():
    try:
        opcaoEscolhida = int(input('Escolha uma opção: '))
        if opcaoEscolhida == 1: 
            nome = input('Digite o nome do livro a ser cadastrado: ')
            categoria = input(f'Digite a categoria do livro {nome}: ')
            Livro.cadastrarLivro(nome, categoria, False)
        elif opcaoEscolhida == 2: 
            Livro.listarLivros()
        elif opcaoEscolhida == 3: 
            nome = input('Digite o nome do livro que deseja alterar o status: ')
            if not Livro.alterarLivro(nome):
                print('O livro não foi encontrado')
        elif opcaoEscolhida == 4: 
            nome = input('Digite o nome do livro que deseja remover: ')
            if not Livro.removerLivro(nome):
                print("Livro não encontrado.")
        elif opcaoEscolhida == 5: 
            finalizar()
            return False
        else: 
            opcaoInvalida()
    except:
        opcaoInvalida()
    return True

#Aqui estarão as funções que main() "puxará"
def main():
    os.system('cls')
    exibirNomePrograma()
    continuar = True
    while continuar:
        exibirOpcoes()
        continuar = escolherOpcao()