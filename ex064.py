soma = 0
qtd = 0
num = 0
while num != 999:
    soma += num
    num = int(input('Digite um número: '))
    if num != 999:
        qtd += 1
print('Soma: {}\nQuantidade: {}'.format(soma, qtd))
