pessoas = list()
tot = 0
media = 0
while True:
    cad = list()
    cad.append(str(input('Digite o nome: ').strip()))
    cad.append(float(input('Digite o peso: ')))
    media += cad[1]
    pessoas.append(cad[:])
    cad.clear()
    tot += 1
    resp = ''
    while True:
        resp = str(input('Deseja continuar [S/N]? ').upper())
        if resp == 'S' or resp == 'N':
            break
    if resp == 'N':
        break
media /= tot
print(f'Foram cadastradas {tot} pessoas. A média de peso é {media}')
print('Lista de pessoas pesadas (acima da média)')
for p in pessoas:
    if p[1] > media:
        print(p[0])
print('Lista de pessoas leves (igual ou abaixo da média)')
for p in pessoas:
    if p[1] <= media:
        print(p[0])
