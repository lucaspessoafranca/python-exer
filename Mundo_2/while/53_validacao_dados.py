#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite o seu Sexo [M/F]')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('Digite o seu Sexo [M/F]')).upper().strip()[0]
print(f'Sexo {sexo} registrado com sucesso')


