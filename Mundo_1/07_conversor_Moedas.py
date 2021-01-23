#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = int(input("Quantos reais você tem na carteira?"))
dolar = real / 5
print(f'Com {real} R$ você pode comprar {dolar:.0f} $ dolares')