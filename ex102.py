def fatorial(n, show=False):
    """
    ->Calcula o fatorial de um número
    :param n: número que será calculado
    :param show: True para mostrar o calculo, False para n mostrar
    :return: O valor do fatorial do número informado
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return f


print(fatorial(6, True))
help(fatorial)
