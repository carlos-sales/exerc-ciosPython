num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))
tupla = (num1, num2, num3, num4)
print(f'O número 9 aparece {tupla.count(9)} vez(es)')
if 3 in tupla:
    resp = 'aparece na posição ' + str(tupla.index(3) + 1)
else:
    resp = 'não aparece'
print(f'O número 3 {resp}')
print('Os números pares digitados foram ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
