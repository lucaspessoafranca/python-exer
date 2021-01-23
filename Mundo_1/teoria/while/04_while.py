i = 0

while i <= 10:
    print(i)
    i += 1
print('FIM!')

import os


carros = []
carro = str(input('Digite o nome do carro:'))
while carro != "-1":
    carros.append(carro)
    carro = str(input('Digite o nome do carro:'))
 #limpa a tela 
os.system('cls')
for x in carros:
    print(x)

'''c = 0
tam = len(carros)

while c < tam:
    print(carros[c])
    c += 1'''