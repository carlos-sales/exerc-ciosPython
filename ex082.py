numeros = list()
pares = list()
impares = list()
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = ''
    while True:
        resp = str(input('Deseja continuar [S/N]? ').upper())
        if resp == 'S' or resp == 'N':
            break
    if resp == 'N':
        break
print(f'Lista completa: {numeros}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')
