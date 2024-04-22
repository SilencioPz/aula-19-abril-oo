# Referências
from Locadora.avaliacaoJogo import AvaliacaoJogo
from Locadora.jogo import Jogo
from Locadora.Estrutura.itemCatalogo import ItemCatalogo
from Locadora.Estrutura.jogoSuperNintendo import JogoSuperNintendo
from Locadora.Estrutura.jogoGenesis import JogoGenesis

locadoraBrunim = Jogo('Brunim', 'Diversão')
jogoSuperNintendo = JogoSuperNintendo('Super Mario World', 5.0,'98 fases em um jogo completaço! :D')
jogoSuperNintendo.aplicarDesconto()
jogoGenesis = JogoGenesis('Sonic the Hedgehog 2',4.50,'O melhor jogo de plataforma do Porco Espinho Azul! ^_^')
jogoGenesis.aplicarDesconto()
locadoraBrunim.adicionarNoCatalogo(jogoSuperNintendo)
locadoraBrunim.adicionarNoCatalogo(jogoGenesis)

def main():
    locadoraBrunim.exibirCatalogo

if __name__ == '__main__':
    main()