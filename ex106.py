def printFormatado(msg, cor='none'):
    normal = '\033[0;0m'
    if cor == 'lilas':
        cor = '\033[1;103m'
    elif cor == 'vermelho':
        cor = '\033[41m'
    elif cor == 'azul':
        cor = '\033[44m'
    else:
        cor = normal
    n = len(msg) + 4
    print(f'{cor}~'*n)
    print(f'{msg:^{n}}')
    print('~' * n)
    print(f'{normal}', end='')


def meAjuda(ajuda):
    print('\033[;7m', end='')
    help(ajuda)
    print('\033[0;0m', end='')


while True:
    printFormatado('SISTEMA DE AJUDA PyHELP', 'lilas')
    ajuda = str(input('Função ou biblioteca >'))
    if ajuda.upper() != 'FIM':
        frase = "Acessando manual do comando '" + ajuda + "'"
        printFormatado(frase, 'azul')
        meAjuda(ajuda)
    else:
        printFormatado('ATÉ LOGO!', 'vermelho')
        break
