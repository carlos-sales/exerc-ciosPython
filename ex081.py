numeros = list()
qtd = 0
cinco = False
while True:
    numeros.append(int(input('Digite um número: ')))
    qtd += 1
    if numeros[-1] == 5:
        cinco = True
    resp = ''
    while True:
        resp = str(input('Deseja continuar [S/N]? ').upper())
        if resp == 'S' or resp == 'N':
            break
    if resp == 'N':
        break
print(f'Você digitou {qtd} números')
print(f'Os valores em ordem decrescente são: {sorted(numeros, reverse = True)}')
if cinco:
    print('O número 5 foi digitado!')
else:
    print('Não houve ocorrência de número 5')
