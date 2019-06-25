def area(larg, alt):
    return larg * alt


print(f'{"Controle de Terrenos":^30}')
print('-' * 30)
b = float(input('LARGURA (m): '))
h = float(input('COMPRIMENTO (m): '))
print(f'A área de um teerno {b} x {h} é {area(b, h):.2f} m²')
