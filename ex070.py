prodBarato = ''
menorValor = 99999999
qtd = 0
total = 0
while True:
    prod = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor: R$ '))
    if valor < menorValor:
        prodBarato = prod
        menorValor = valor
    if valor > 1000:
        qtd += 1
    total += valor
    while True:
        resp = str(input('Deseja continuar? [S/N]').upper())
        print('-'*20)
        if resp == 'N' or resp == 'S': break
    if resp == 'N': break
print('---- FIM DE CADASTRO ----')
print(f'Valor gasto: R$ {total:.2f}')
print(f'Produto mais barato: {prodBarato}')
print(f'Quantidade de produtos acima de R$ 1000.00: {qtd}')
