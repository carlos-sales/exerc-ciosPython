val = float(input('Digite o valor do produto: R$ '))
print('{:-^27}'.format('PAGAMENTO'))
print('| 1- À vista              |')
print('| 2- À vista no cartão    |')
print('| 3- 2x no cartão         |')
print('| 4- 3x ou mais no cartão |')
op = int(input(' ------- Escolha a opção: '))

if op == 1:
    vpagar = val * 0.9
elif op == 2:
    vpagar = val * 0.95
elif op == 3:
    vpagar = val
elif op == 4:
    vpagar = val * 1.2
else:
    print('Opção inválida')

print('O valor a pagar será: R$ {:.2f}'.format(vpagar))
