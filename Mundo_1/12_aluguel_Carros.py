#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = float(input('Quantos dias :'))
km = float(input("KM percorridos:"))
total = (dias * 60) + (km * 0.15)
print(f'Um carro para {dias}dias com {km}KM percorridos, custará {total:.2f}R$') 