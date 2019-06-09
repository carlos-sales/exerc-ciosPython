termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
print('1º termo: {}'.format(termo))
for i in range(1, 10):
    print('{}º termo: {}'.format(i+1, termo+(razao*i)))
