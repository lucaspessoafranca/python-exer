#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint 
n = (randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10),randint(1, 10))
print(f'Eu sorteei os valores {n}')
for c in n:
    print(f'{n}')
print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')