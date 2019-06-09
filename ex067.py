while True:
    n = int(input('Deseja ver a tabuada de qual valor? '))
    if n < 0: break
    print('-'*20)
    print(f'Tabuada de {n}')
    print('-' * 20)
    for i in range(1, 10):
        print(f'{n} x {i} = {n * i}')
    print('-' * 20)
