def contador(i,f,p):
    """

    :param i: inicio
    :param f: fim
    :param p: passo ( ex: 2 em 2)
    :return:
    """
    c = i
    while c <=f:
        print(f'{c}, end='')
        c+= p
    print('FIM')

contador(2,10,2)