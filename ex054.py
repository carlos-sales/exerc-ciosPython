from datetime import datetime
ano = datetime.now()
n = 0
for i in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}º pessoa: '.format(i)))
    if ano.year - nasc > 18:
        n += 1
print('Número de pessoas maiores de idade: {}'.format(n))
