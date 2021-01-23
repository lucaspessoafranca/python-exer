#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Largura da parede'))
altura = float(input('Altura da parede'))
area = largura * altura 
print(f' Para pintar uma parede com {largura}x{altura} a aréa será de {area}m2')
tinta = area / 2
print(f'Para pintar essa parede, será preciso {tinta}L de tinta') 