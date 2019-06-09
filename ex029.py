vel = float(input('Digite a velocidade (km/h): '))
if vel > 80:
    status = 'Multado!'
    multa = (vel - 80) * 7
else:
    status = 'Sem multa'
    multa = 0
print('Status: {}'.format(status))
print('Multa: R$ {:.2f}'.format(multa))
