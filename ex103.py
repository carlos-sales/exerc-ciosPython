def ficha(n="<desconhecido>", g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato')


nome = str(input('Nome do jogador: ').strip())
gols = input('Número de gols: ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = ''
if nome != '' and gols != '':
    ficha(nome, gols)
elif nome != '':
    ficha(nome)
elif gols != '':
    ficha(g=gols)
else:
    ficha()
