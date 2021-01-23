#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

#5! = 5 x 4 x 3 x 2 x 1 = 120

'''from math import factorial
n = int(input('Digite o número '))
fatorial = factorial(n)
print(f'O fatorial de {n} é {fatorial}')'''
n = int(input('Digite um número para saber o seu fatorial'))
c = n
f = 1
print(f'Calculando {n}! = ',end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='' )
    f *= c
    c -= 1
print('{}'.format(f))