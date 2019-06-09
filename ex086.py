matriz = list()
for i in range(0, 3):
    num = list()
    for j in range(0, 3):
        num.append(int(input(f'Digite o valor para a posição [{i}][{j}] : ')))
    matriz.append(num[:])
    num.clear()
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]:^5} ]', end='')
    print('')
