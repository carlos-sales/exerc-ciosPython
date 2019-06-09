numeros = list()
for i in range(0, 5):
    num = int(input('Digite um número: '))
    j = i
    while True:
        if len(numeros) == 0 or num > numeros[-1]:
            numeros.append(num)
            print('Adicionado no final da lista!')
            break
        elif num > numeros[j-1]:
            numeros.insert(j, num)
            print(f'Adicionado na {j}º posição')
            break
        elif j == 1:
            numeros.insert(0, num)
            print('Esse agora é o primeiro item da lista')
            break
        else:
            j -= 1
print(f'Lista de números {numeros}')
