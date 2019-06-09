num = int(input('Digite um número: '))
for i in range(2, num):
    if i+1 == num:
        print('O número digitado É PRIMO')
    elif num%i == 0:
        print('O número digitado NÃO É PRIMO')
        break
print('FIM')
