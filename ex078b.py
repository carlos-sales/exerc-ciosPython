numeros = list()
maior = ''
menor = ''
for i in range(0, 5):
    numeros.append(int(input(f'Digite a {i}º posição da lista: ')))
for pos, i in enumerate(numeros):
    if i == max(numeros):
        maior += str(pos) + ' '
    if i == min(numeros):
        menor += str(pos) + ' '
print(f'Maior: {max(numeros)} | Posição(ôes): {maior}')
print(f'Menor: {min(numeros)} | Posição(ôes): {menor}')
