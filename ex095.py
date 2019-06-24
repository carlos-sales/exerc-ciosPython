jogadores = list()
jog = dict()
gols = list()
while True:
    jog.clear()
    jog['nome'] = str(input('Nome: ').strip())
    partidas = int(input(f'Quantas partidas fez {jog["nome"]}? '))
    gols.clear()
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols fez {jog["nome"]} na partida {i+1}? ')))
    jog['gols'] = gols[:]
    jog['total'] = sum(gols)
    jogadores.append(jog.copy())
    while True:
        resp = str(input('Deseja continuar [S/N]? ').upper())
        if resp in 'SN':
            break
        print('ERRO: Responda com S ou N')
    if resp == 'N':
        break
print('-' * 50)
print(f'{"Cod":<5}{"Nome":<20}{"Gols":<20}{"Total":<5}')
print('-' * 50)
for i, v in enumerate(jogadores):
    print(f'{i:<5}{v["nome"]:<20}{str(v["gols"]):<20}{v["total"]:<5}')
print('-' * 50)
while True:
    op = int(input('Mostrar detalhes de qual jogador [999 para sair]? '))
    if op == 999:
        break
    elif op >= len(jogadores):
        print(f'CÓDIGO INVÁLIDO! Não existe jogador com o código {op}')
    else:
        print(f'- LEVANTAMENTO DE GOLS DO JOGADOR: {jogadores[op]["nome"]}')
        for i, v in enumerate(jogadores[op]['gols']):
            print(f'    -> Na partida {i+1} fez {v} gol(s)')
