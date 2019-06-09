maior = 0
menor = 999999
for i in range(1, 6):
    peso = float(input('Digite o peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso digitado foi: {} kg'.format(maior))
print('O menor peso digitado foi: {} kg'.format(menor))
