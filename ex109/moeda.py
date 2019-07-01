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
