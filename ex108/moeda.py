def metade(n):
    return n / 2


def dobro(n):
    return n * 2


def aumentar(n, porc):
    """
    -> função para aumentar, em um número, x porcento
    :param n: valor base para calculo
    :param porc: porcentagem a ser incrementada
    :return: retorna o numero atualizado
    """
    return n + (n * porc / 100)


def moeda(val, moeda="R$"):
    return f'{moeda} {val:.2f}'.replace('.', ',')

