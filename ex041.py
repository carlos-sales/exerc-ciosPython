from datetime import date
ano = int(input('Digite o ano de nascimento: '))
ano = date.today().year

if ano <= 9:
    print('Mirim')
elif ano <= 14:
    print('Infantil')
elif ano <= 19:
    print('Júnior')
elif ano == 20:
    print('Sênior')
else:
    print('Master')
