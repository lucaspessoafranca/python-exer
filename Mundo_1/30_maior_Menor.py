# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input("Digite o primeiro número"))
n2 = int(input("Digite o segundo número"))
n3 = int(input("Digite o terceiro número"))
# verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
# verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n2 and n3 < n1:
    menor = n3
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')
