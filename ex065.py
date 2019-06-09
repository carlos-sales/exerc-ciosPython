qtd = 0
maior = 0
menor = 9999999
media = 0
resp = 'S'
while resp == 'S':
    num = int(input('Digite um número: '))
    media += num
    qtd += 1
    if num < menor: menor = num
    if num > maior: maior = num
    resp = str(input('Deseja continuar? [S/N] ').upper())
print('MÉDIA: {}\nMAIOR: {}\nMENOR: {}'.format(media/qtd, maior, menor))
