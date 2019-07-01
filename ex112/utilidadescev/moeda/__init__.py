def metade(n, format=False):
    if format:
        return moeda(n / 2)
    return n / 2


def dobro(n, format=False):
    if format:
        return moeda(n * 2)
    return n * 2


def aumentar(n, porc, format=False):
    """
    -> função para aumentar, em um número, x porcento
    :param n: valor base para calculo
    :param porc: porcentagem a ser incrementada
    :param format: formata moeda
    :return: retorna o numero atualizado
    """
    if format:
        return moeda(n + (n * porc / 100))
    return n + (n * porc / 100)


def diminuir(n, porc, format=False):
    """
    -> função para decrementar, em um número, x porcento
    :param n: valor base para cálculo
    :param porc: porcentagem a ser decrementada
    :param format: formata moeda
    :return: retorna o numero atualizado
    """
    if format:
        return moeda(n - (n * porc / 100))
    return n - (n * porc / 100)


def moeda(val, moeda="R$"):
    return f'{moeda} {val:.2f}'.replace('.', ',')


def resumo(n, aum, dim):
    print('-' * 35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-' * 35)
    print(f'{"Preço analisado:":<25}{moeda(n):<15}')
    print(f'{"Dobro do preço:":<25}{dobro(n, True):<15}')
    print(f'{"Metade do preço:":<25}{metade(n, True):<15}')
    print(f'{str(aum) + " de aumento:":<25}{aumentar(n, aum, True):<15}')
    print(f'{str(dim) + " de redução:":<25}{diminuir(n, dim, True):<15}')
