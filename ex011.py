lar = float(input('Digite a largura (em metros): '))
alt = float(input('Digite a altura (em metros): '))
area = lar * alt
print('Serão necessários {:.2f} litros de tinta pra pintar essa parede'.format(area/2))
