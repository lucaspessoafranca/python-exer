# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número'))
print(''' Escolha uma das bases para conversão:
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
resposta = int(input(''))
if resposta == 1:
    print(f'O número {num} convertido para BINÁRIO é {bin(num)[2:]}')
elif resposta == 2:
    print(f'O número {num} convertido para OCTAL é {oct(num)[2:]}')
elif resposta == 3:
    print(f'O número {num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Opção inválida, Tente Novamente!')


    
