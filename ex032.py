from datetime import date
ano = int(input('Digite o ano: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    if ano % 100 != 0 or (ano % 100 == 0 and ano % 400 == 0):
        print('É bissexto')
    else:
        print('Não é bissexto!')
else:
    print('Não é bissexto ', ano)
