from time import sleep


def analisador(*num):
    maior = -999
    print('-=' * 50)
    print('Analisando os valores:')
    for i in num:
        print(i, end=' ')
        sleep(0.3)
        if i > maior:
            maior = i
    print(f'Foram informados {len(num)} números')
    print(f'O maior número informado foi {maior}')


analisador(2, 6, 4, 1, 10, 5, 8)
analisador(8, 9, 74, 0)
analisador(20, 30, 5, 6, 8, 9, 7, 8, 10, 9, 6)
