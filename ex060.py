num = int(input('Digite o número: '))
res = 1
fat = ''
while num != 0:
    res *= num
    if num > 1: fat += str(num) + 'x'
    else: fat += str(num) + '='
    num -= 1
print('{} {}'.format(fat, res))
