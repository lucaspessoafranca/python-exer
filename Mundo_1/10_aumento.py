#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe o salário do funcionário R$:'))
novoSalario = salario + (salario * 0.15)
print(f'O novo salário do funcionário com 15% de aumento será: {novoSalario}R$')