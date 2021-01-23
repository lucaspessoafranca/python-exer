#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.z

produto = float(input('Preço do produto?'))
desconto = produto - (produto*0.05)
print(f'O novo preço do produto com 5% de desconto é {desconto} ')