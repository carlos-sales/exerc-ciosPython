numeros = []
par = []
impar = []
for i in range(1, 8):
    num = int(input(f'Digite o {i}º valor: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
numeros.append(sorted(par))
numeros.append(sorted(impar))
print(f'Os valores pares digitados foram {numeros[0]}')
print(f'Os valores impares digitados foram {numeros[1]}')
