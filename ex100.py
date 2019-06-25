from random import randint
from time import sleep


def sorteia(lst_num):
    print('Sorteando 5 valores: ', end=' ')
    for i in range(0, 5):
        n = randint(0, 10)
        print(n, end=' ')
        lst_num.append(n)
        sleep(0.3)
    print()


def somaPar(num):
    soma = 0
    for i in num:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos pares na lista {num} é igual a {soma}')
    print('-' * 60)

numeros = list()
sorteia(numeros)
somaPar(numeros)
