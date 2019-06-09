from datetime import date
idade = int(input('Digite o ano de nascimento: '))
idade = date.today().year - idade

if idade < 18:
    print('Falta(m) {} ano(s) para você se alistar'.format(18-idade))
elif idade == 18:
    print('Tá na hora de se alistar')
else:
    print('Você deveria ter se alistado há {} ano(s)'.format(idade-18))
