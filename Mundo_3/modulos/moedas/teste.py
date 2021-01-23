'''Modifique as funções que form criadas no desafio 107
para que elas aceitem um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

from moedas import moeda

p = float(input('Digite o preço R$:'))
print(f'A metade {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(,True)}')
print(f' Aumentando 10%, temos {moeda.aumenta(p,10,True)}')