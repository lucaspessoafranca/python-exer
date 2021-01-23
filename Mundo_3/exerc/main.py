'''
Crie um módulo chamado moeda.py
 que tenha as funções incorporadas aumentar()
 , diminuir(), dobro() e metade().
  Faça também um programa que importe esse módulo
   e use algumas dessas funções
'''
#import moeda
import moeda
#import exerc.moeda
#from exerc import moeda

p = float(input('Digite o preço R$'))
print(f'A meta de {p:.2f} é : {moeda.metade(p)}')
print(f'O dobro de R${p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumenta(p,10)}')