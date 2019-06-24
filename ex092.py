from datetime import date
cadastro = dict()
cadastro['nome'] = str(input('Nome: ').strip())
ano = int(input('Ano de nascimento: '))
cadastro['idade'] = date.today().year - ano
cadastro['ctps'] = str(input('Carteira de trabalho [caso não tenha, digite 0]: '))
cadastro['aposenta'] = cadastro['idade'] + 35
if cadastro['ctps'] != '0':
    cadastro['ano_contrat'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    cadastro['aposenta'] -= (date.today().year - cadastro['ano_contrat'])
print('*' * 30)
print('{:^30}'.format('Resultado'))
print('*' * 30)
for k, v in cadastro.items():
    print(f'    {k} : {v}')
