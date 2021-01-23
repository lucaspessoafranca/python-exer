#Crie um programa que faça o computador jogar Jokenpô com você
from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador= int(input('qual você escolhe?'))
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
if computador == 0:# pedra
    if jogador == 0: #pedra
        print('EMPATE!')
    elif jogador == 1:
        print('jogador vence!')
    elif jogador == 2:
        print('Computador Vence!')
    else:
        print('Jogada inválida!')
elif computador == 1: # computador papel
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador vence!')
    else:
        print('Jogada inválida!')
elif computador == 2:#computador jogou tesoura
    if jogador == 0:
        print('Jogador Vence!')
    elif jogador == 1:
        print('Computador vence!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida!')

