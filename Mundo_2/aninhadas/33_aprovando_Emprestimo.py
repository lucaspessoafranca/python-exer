# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input("Em quantos anos deseja financiar?"))
prestacao = casa / (anos * 12)
min = salario * 30 / 100
print(
    f'Para pagar uma casa de {casa:.2f} em {anos} a prestação será de {prestacao:.2f}')
if prestacao <= min:
    print('Empréstimo pode ser APROVADO!!')
else:
    print('Empréstimo NEGADO!')
