sal = float(input('Digite o salário: R$ '))
if sal < 1250:
    sal *= 1.15
else:
    sal *= 1.1
input('Salário reajustado: R$ {:.2f}'.format(sal))
