# arquivo para testar módulos e pacotes dos exercícios 107 a 112
# ~~ EXERCÍCIO 107 ~~
# from ex107 import moeda

# p = float(input('Digite o preço: R$ '))
# print(f'A metade de {p} é {moeda.metade(p)}')
# print(f'O dobro de {p} é {moeda.dobro(p)}')
# print(f'Aumentando 10%, temos {moeda.aumentar(p, 10):.2f}')
# print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13):.2f}')

# ~~ EXERCÍCIO 108 ~~
# from ex108 import moeda

# p = float(input('Digite o preço: R$ '))
# print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
# print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
# print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')

# ~~ EXERCÍCIO 109 ~~
# from ex109 import moeda

# p = float(input('Digite o preço: R$ '))
# print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
# print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
# print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
# print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, False)}')

# ~~ EXERCÍCIO 110 ~~
# from ex110 import moeda

# p = float(input('Digite um valor: R$ '))
# moeda.resumo(p, 80, 35)

# ~~ EXERCÍCIO 111 ~~
# from ex111.utilidadescev import moeda

# p = float(input('Digite um valor: R$ '))
# moeda.resumo(p, 80, 35)

# ~~ EXERCÍCIO 112 ~~
from ex112.utilidadescev import dado, moeda

p = dado.leiaDinheiro('Digite um valor: R$ ')
moeda.resumo(p, 80, 35)
