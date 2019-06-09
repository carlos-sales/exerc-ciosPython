num = int(input('Digite o número que deseja saber a tabuada de 1 a 10: '))
for i in range(1, 11):
    print('{} X {} = {}'.format(num, i, num*i))
