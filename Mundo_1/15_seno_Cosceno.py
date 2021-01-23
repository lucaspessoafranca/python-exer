# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#  cosseno e tangente desse ângulo.
from math import sin, radians, cos, tan
an = float(input("Digite o ângulo que você deseja"))
seno = sin(radians(an))
print(f'O ângulo de {an} tem o SENO de {seno:.2f}')
cosseno = cos(radians(an))
print(f'O ângulo de {an} tem o SENO de {cosseno:.2f}')
tangente =  tan(radians(an))
print(f"O Ângulo de {an} tem a TANGENTE de {tangente:.2f}")


