# Aprimore o desafio anterior, mostrando no final: 
 #A) A soma de todos os valores pares digitados.  
#B) A soma dos valores da terceira coluna.     
#) O maior valor da segunda linha.
                                                                                                  #         C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] :'))
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'Asoma dos valores pares é {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dosvalroes da terceira coluna é {scol}')
for c in range (0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior alor da segunda linha é {mai}')