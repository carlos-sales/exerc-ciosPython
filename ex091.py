from time import sleep
from random import randint
from operator import itemgetter
jogo = {'JOGADOR 1': randint(1, 6),
        'JOGADOR 2': randint(1, 6),
        'JOGADOR 3': randint(1, 6),
        'JOGADOR 4': randint(1, 6)}
print('JOGANDO DADOS')
for k, v in jogo.items():
    print(f'    {k} tirou {v}')
    sleep(1)
ranking = ()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=*' * 5)
print('RANKING')
for i, v in enumerate(ranking):
    print(f'    {i+1}º Lugar: {v[0]} tirou {v[1]}')
    sleep(1)
