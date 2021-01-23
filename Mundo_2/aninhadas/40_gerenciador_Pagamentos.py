# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal

# – 3x ou mais no cartão: 20% de juros

produto = float(input('Valor a ser pago pelo produto:'))
print(''' Opções de pagamento
[1] - à vista dinheiro /cheque [10% de desconto]
[2] - à vista no cartão  [5% de desconto]
[3] - 2x no cartão [ preço normal]
[4] - 3x ou mais no cartão [20% de juros]''')
opcao = int(input('Qual é a sua escolha?'))
if opcao == 1:
    preco = produto - (produto * 10 / 100)
    print(f'O produto que custa {produto} com 10% de desconto custará {preco}')
elif opcao == 2:
    preco = produto - (produto * 5 / 100)
    print(f'O produto que custa {produto} com 5% de desconto custará {preco}')
elif opcao == 3:
    preco = produto / 2
    print(
        f'O produto que custa {produto} será parcelado em 2x de {preco} no cartão')
elif opcao == 4:
    parcela = int(input('Em quantas vezes você deseja parcelar?'))
    preco = produto + (produto * 20/100)
    juros = preco / parcela
    print(
        f'O produto que custa {produto} será parcelado em {parcela} vezes de {juros} e custará {preco} com JUROS')
