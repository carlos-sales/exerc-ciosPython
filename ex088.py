from random import randint
from time import sleep
print('-'*50)
print('{:^50}'.format('JOGA NA MEGA SENA'))
print('-'*50)
qtd = int(input('Quantos jogos você quer que sejam gerados? '))
print(f'{"-="*5} SORTEANDO {qtd} JOGOS {"-="*5}')
for i in range(1, qtd+1):
    jogo = list()
    while len(jogo) <= 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    sleep(1)
    print(f'JOGO {i}: {sorted(jogo)}')
print(f'{"-="*6} <BOA SORTE!> {"-="*6}')
