n = int(input('Informe um número: '))
num = str(n)
print('Analisando o numero ', num)
print('Unidade: {}'.format(num[0]))
print('Dezena: {}'.format(num[1]))
print('Centena: {}'.format(num[2]))
print('Milhar: {}'.format(num[3]))

num2 = int(input('Informe um número: '))
u = num2 // 1 % 10
d = num2 // 10 % 10
c = num2 // 100 % 10
m = num2 // 1000 % 10
print('Analisando o numero ', num2)
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))