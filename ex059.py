num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
op = 0
res = 0
while op != 5:
    print('{:-^22}'.format(' MENU '))
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    op = int(input('----- OPÇÃO DESEJADA: '))
    if op == 1:
        res = num1 + num2
        print('A soma entre {} e {} é igual a {}'.format(num1, num2, res))
    elif op == 2:
        res = num1 * num2
        print('A multiplicação entre {} e {} é igual a {}'.format(num1, num2, res))
    elif op == 3:
        if num1 > num2: print('O número {} é maior que {}'.format(num1, num2))
        else: print('O número {} é maior que {}'.format(num2, num1))
    elif op == 4:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
    elif op == 5:
        print('Saindo!')
    else:
        print('Opção inválida!')
