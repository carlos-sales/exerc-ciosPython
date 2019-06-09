val = float(input('Diz aí, quantos reais você tem? R$ '))
print('Com esse valor dá pra comprar', end=' US$ ')
print('{:.2f}'.format(val/3.27))
