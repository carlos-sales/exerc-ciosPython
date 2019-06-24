jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do Jogador: ').strip())
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {i+1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('*' * 30)
print(jogador)
print('*' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('*' * 30)
print(f'{jogador["nome"]} jogou {partidas} partidas: ')
for i, v in enumerate(gols):
    print(f'    --> Na partida {i+1}, fez {v} gol(s);')
print(f'Totalizando {jogador["total"]} gols')
