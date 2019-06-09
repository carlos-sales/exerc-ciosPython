mais18 = homens = m20 = 0
while True:
    while True:
        pSexo = str(input('Digite o sexo [M/F]: ').upper())
        if pSexo == 'M' or pSexo == 'F': break
    # o While acima pode ser feito da seguinte forma:
    # pSexo = ' '
    # while pSexo not in 'MF':
    #   pSexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    pIdade = int(input('Digite a idade da pessoa: '))
    if pIdade > 18: mais18 += 1
    if pSexo == 'M': homens += 1
    elif pIdade < 20: m20 += 1
    while True:
        resp = str(input('Deseja continuar [S/N]? ').upper())
        if resp == 'N' or resp == 'S': break
    if resp == 'N': break
    print('-'*10)
print('----- FIM DO CADASTRO -----')
print(f'Pessoas com mais de 18 anos: {mais18}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {m20}')
