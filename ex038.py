num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O {} é maior'.format(num1))
elif num2 > num1:
    print('O {} é maior'.format(num2))
else:
    print('Os números são iguais')
