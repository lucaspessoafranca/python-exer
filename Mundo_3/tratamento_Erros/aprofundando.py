def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO:  Por favor, digite um número inteiro válido: \033[m')
            continue #volta pro While
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usúario\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO:  Por favor, digite um número inteiro válido: \033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsúario interrompeu a entrada de dados.\033[m')
            return 0
        else:
            return n







n1 = leiaInt('Digite um \033[034m número INTEIRO:\033[m')
n2 = leiaFloat('Digite um \033[035m número REAL \033[m')
print(f'\nO valor INTEIRO digitado foi {n1}\n O valor REAL digitado foi : {n2}')
