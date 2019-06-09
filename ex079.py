numeros = list()
while True:
    num = int(input('Digite um número: '))
    if not num in numeros:
        numeros.append(num)
        print('Número inserido!')
    else:
        print('Não vou inserir, pois já consta o número na lista')
    resp = ''
    while True:
        if resp != 'S' and resp != 'N':
            resp = str(input('Deseja continuar [S/N?] ').upper())
        else:
            break
    if resp == 'N':
        break
numeros.sort()
print(f'Números digitados: {numeros}')
