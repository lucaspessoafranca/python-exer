galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: M/F')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print(f'ERRO! por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade'))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N')
    if resp == 'N':
        break
print(f'A) ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ' , end='')
for p in galera:
    if ['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='' )
print()
print('D) Lista de pessoas que estão acima da média :')
for p in galera:
    if p['idade'] >= media:
        print( '    ')
        for k, v in p.items():
            prin(f'{k} = {v}', end='')
        print()
