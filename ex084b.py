pessoas = list()
tot = 0
maior = 0
menor = 9999
while True:
    cad = list()
    cad.append(str(input('Digite o nome: ').strip()))
    cad.append(float(input('Digite o peso: ')))
    if maior < cad[1]:
        maior = cad[1]
    if menor > cad[1]:
        menor = cad[1]
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
print(f'Foram cadastradas {tot} pessoas')
print(f'O maior peso foi {maior} Kg, peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso foi {menor} Kg, peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
