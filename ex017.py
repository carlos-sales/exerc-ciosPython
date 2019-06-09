from math import hypot
cat = float(input('Digite o valor do cateto: '))
adj = float(input('Digite o valor do adjacente: '))
hip = hypot(cat, adj)
print('A hpotenusa vale: {}'.format(hip))
