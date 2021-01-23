'''carros = ["Gol","Honda"]

i = 0
tam = len(carros)

while i < tam:
    print(carros[i])
    i+=1
print('FIM')'''
import os
carros = []
carro = input('Digite o nome do novo carro')

while carro != '-1':
    carros.append(carro)
    carro = input('Digite o nome do novo carro : ')

os.system('cls')
for x in carros:
    print(x)

print('\n Fim do loop')