#Crie um programa que leia o nome de uma pessoa 
# e diga se ela tem “SILVA” no nome.

nome = str(input("Digite o seu nome:")).strip()
#verifica = ('silva' in nome.lower())
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))