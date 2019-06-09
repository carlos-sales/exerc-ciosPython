from random import randint
numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
maior = 0
menor = 101
for i in numeros:
    print(f'{i}', end=' ')
print(f'\nMaior: {max(numeros)}\nMenor: {min(numeros)}')
