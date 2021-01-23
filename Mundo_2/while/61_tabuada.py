#cria uma tabuada usando a estrutura while
while True:
    n = int(input('Digite um número :'))
    if n < 0:
        break
    print('-' * 30)
    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
    