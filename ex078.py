numeros = list()
for i in range(0, 5):
    numeros.append(int(input('Digite um número: ')))
print(f'Maior: {max(numeros)} | Posição(ões): ', end='')
for pos, i in enumerate(numeros):
    if i == max(numeros):
        print(f'{pos} ', end='')
print(f'\nMenor: {min(numeros)} | Posição(ões): ', end='')
for pos, i in enumerate(numeros):
    if i == min(numeros):
        print(f'{pos} ', end='')
