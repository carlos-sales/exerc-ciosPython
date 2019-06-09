matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}][{j}]: '))
        if matriz[i][j] % 2 == 0:
            pares += matriz[i][j]
        if i == 1:
            if maior < matriz[i][j]:
                maior = matriz[i][j]
        if j == 2:
            soma += matriz[i][j]
print(f'Soma pares: {pares}')
print(f'Soma terceira coluna: {soma}')
print(f'Maior segunda linha: {maior}')
