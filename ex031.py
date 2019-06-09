dist = float(input('Digite a distância (em km): '))
if dist <= 200:
    val = dist * 0.5
else:
    val = dist * 0.45
print('Valor da passagem: R$ {:.2f}'.format(val))
