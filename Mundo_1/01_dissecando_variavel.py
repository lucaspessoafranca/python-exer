#Usando seus conhecimentos adquiridos em aulam disseque uma variável
nome = str(input('Digite uma palavra'))
print(f'O tipo primitivo de {nome} é {type(nome)}')
print(f'Só tem espaços? {nome.isspace()}')
print(f'é um número ? {nome.isnumeric()}')
print(f'É alfanumérico? {nome.isalnum()}')
print(f'É alfabético? {nome.isalpha()}')
print(f'Está em maiúsculo? {nome.isupper()}')
print(f'Está em minúsculo? {nome.islower()}' )
print(f'Está capitalizado? {nome.istitle()}')