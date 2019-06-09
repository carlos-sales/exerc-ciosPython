print('='*30)
print('{:^30}'.format('Banco CEV'))
print('='*30)
valor = int(input('Digite o valor a ser sacado: R$ '))
ced = 50
totCed = 0
print('O valor requerido será entregue da seguinte forma:')
while True:
    if valor >= ced:
        valor -= ced
        totCed += 1
    else:
        if totCed > 0:
            print(f'{totCed} notas de R$ {ced:.2f}')
            totCed = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        else:
            break
