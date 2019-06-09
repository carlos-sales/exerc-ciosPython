n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1 > n2 and n1 > n3:
    maior = n1
    if n2 > n3:
        menor = n3
    else:
        menor = n2
elif n2 > n1 and n2 > n3:
    maior = n2
    if n1 > n3:
        menor = n3
    else:
        menor = n1
else:
    maior = n3
    if n1 > n2:
        menor = n2
    else:
        menor = n1
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
