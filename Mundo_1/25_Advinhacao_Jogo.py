# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from time import sleep
from random import randint
jogador = int(input("Digite um número inteiro entre 0 e 5.."))
computador = randint(0, 5)
print('Processando..')
sleep(3)
if jogador == computador:
    print('ACERTOU!!')
else:
    print(f'GANHEI ! Eu escolhi {computador} e não {jogador} ')
