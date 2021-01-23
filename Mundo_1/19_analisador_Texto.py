#Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

from time import sleep
nome = str(input("Digite o seu nome")).strip()
print('Analisando o seu nome...')
sleep(2)
print(f'O seu nome em maiúsculo é {nome.upper()}')
print(f'O seu nome em minúsculo é {nome.lower()}')
corte = (len(nome) - nome.count(' '))
print(f'O seu nome tem ao todo {corte} letras') 
#print(f'Seu primeiro nome tem {nome.find(" ")} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')