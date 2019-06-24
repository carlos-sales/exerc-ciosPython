pessoas = list()
cad = dict()
media = 0
while True:
    cad.clear()
    cad['nome'] = str(input('Nome: ').strip())
    while True:
        cad['sexo'] = str(input('Sexo [M/F]: ').strip().upper()[0])
        if cad['sexo'] in 'MF':
            break
        print('ERRO: Responda com M ou F')
    cad['idade'] = int(input('Idade: '))
    media += cad['idade']
    pessoas.append(cad.copy())
    while True:
        resp = str(input('Deseja continuar [S/N] ? ').upper()[0])
        if resp in 'SN':
            break
        print('ERRO: Responda com S ou N')
    if resp == 'N':
        break
media /= len(pessoas)
print('*' * 30)
print(f'O grupo tem {len(pessoas)} pessoas')
print(f'A média de idade do grupo é {media:.2f} anos')
print('As mulheres cadastradas são: ')
for v in pessoas:
    if v['sexo'] == 'F':
        print(f'    --> {v["nome"]}')
print('Pessoas acima da média de idade do grupo: ')
for v in pessoas:
    if v['idade'] > media:
        print(f'    --> {v["nome"]}')
