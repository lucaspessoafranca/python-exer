'''Modifique as funções que form criadas no desafio 107
para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

#from reduzindo import moeda
#from reduzindo.utilidades import moeda
from reduzindo.utilidades import moeda
from reduzindo.utilidades import dado


p = dado.leiaDinheiro('Digite o Preço:')
moeda.resumo(p,20,12)