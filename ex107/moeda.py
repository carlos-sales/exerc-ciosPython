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


def diminuir(n, porc):
    """
    -> função para decrementar, em um número, x porcento
    :param n: valor base para cálculo
    :param porc: porcentagem a ser decrementada
    :return: retorna o numero atualizado
    """
    return n - (n * porc / 100)
