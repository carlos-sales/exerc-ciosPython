num = int(input('Digite um número: '))
print(' ------ MENU ------ ')
print('| 1 - binário      |')
print('| 2 - octal        |')
print('| 3 - hexadecimal  |')
print(' ------------------ ')
op = int(input('Digite a opção de conversão desejada: '))

if op == 1:
    print('O binário de {} é {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O octal de {} é {}'.format(num, oct(num)[2:]))
else:
    print('O hexadecimal de {} é {}'.format(num, hex(num)[2:]))
