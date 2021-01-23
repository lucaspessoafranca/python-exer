#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* num): # * serve para informar que vou receber vários parâmetros e usar laço para desempaotar
    cont = maior = 0
    print('Analisando os valores passados... ',end='')
    for valor in num:
        print(f'{valor} ',  end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores')
    print(f'O maior valor informado foi {maior}.')


#programa principal
maior(8,4,5)
