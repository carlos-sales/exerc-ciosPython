s = 0
for i in range(1, 7):
    n = int(input('Digite o {}º número: '.format(i)))
    if n%2 == 0:
        s += n
print('A soma dos números pares digitados é: {}'.format(s))
