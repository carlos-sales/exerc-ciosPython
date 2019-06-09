brasileirao = ('Fluminense',
               'São Paulo',
               'Botafogo',
               'Cruzeiro',
               'Grêmio',
               'Internacional',
               'Santos',
               'Palmeiras',
               'Bahia',
               'Fortaleza',
               'Chapecoense',
               'Athlético-PR',
               'Avaí',
               'CSA',
               'Goiás',
               'Ceará',
               'Vasco',
               'Atlético-MG',
               'Corinthians',
               'Flamengo')
print('5 primeiros colocados:')
print(brasileirao[:5])
print('4 últimos que SERÃO REBAIXADOS:')
print(brasileirao[-4:])
print('Tabela em ordem alfabética:')
for i in sorted(brasileirao):
    print(i)
print(f'Posição da Chapecoense: {brasileirao.index("Chapecoense")+1}')
