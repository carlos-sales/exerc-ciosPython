lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livro', 34.9)
print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)
for pos, i in enumerate(lista):
    if pos % 2 == 0:
        print(f'{i:.<31}', end='R$')
    else:
        print(f'{i:7.2f}')
print('-'*40)
