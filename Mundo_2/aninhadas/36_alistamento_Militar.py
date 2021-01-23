# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
nasc = int(input("Ano de nascimento: "))
anoAtual = date.today().year
idade = anoAtual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos atualmente')
if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE !')
elif idade < 18:
    saldo = 18 - idade
    print(f'ainda faltam {saldo} anos para o seu alistamento')
    alistamento = anoAtual + saldo
    print(f'Seu alistamento será  em {alistamento} ')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos')
    alistamento = anoAtual - saldo
    print(f'Seu alistamento foi em {alistamento} ')
