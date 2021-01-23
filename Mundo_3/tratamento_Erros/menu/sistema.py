from menu.lib.interface import *
cabecalho('SISTEMA 1.0')
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Pessoas',  'Sair do Programa'])
    if resposta == 1:
        cabecalho('Opcão 1')
    elif resposta == 2:
        cabecalho('Opção 2')
    elif resposta == 3:
        cabecalho('Saindo do sistema.')
        break
    else:
        print('Erro! digite uma opção válida')