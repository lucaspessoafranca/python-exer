# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o seu salário:'))
if salario > 1250:
    aumento = salario + (salario*0.10)
    print(f'Seu novo salário com aumento de 10% SERÁ R${aumento}')

elif salario <= 1250:
    aumento = salario + (salario*0.15)
    print(f'Seu novo salário com aumento de 15% SERÁ R${aumento}')
