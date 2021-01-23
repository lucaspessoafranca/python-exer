#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento)
#  e mostre a área do terreno.

def area(largura,comprimento):
    a = largura * comprimento 
    print(f'A área de u m terreno de {largura:.2f}x{comprimento:.2f} é de {a} m2')


print('Controle de Terrenos')
print('-' * 30)
l = float(input('Largura (m) '))
c = float(input('Comprimento (m) '))
area(l,c)