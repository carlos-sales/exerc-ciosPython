from time import sleep


def contador(ini, f, p):
    aux = 1
    if p == 0:
        p = 1
    if ini > f and p > 0:
        p *= -1
    if p < 0:
        aux *= -1
    print(f'Contagem de {ini} até {f} de {p} em {p}')
    for i in range(ini, f+aux, p):
        print(i, end=' ')
        sleep(0.5)
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('--- Personalize o contador ---')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
pulo = int(input('Pulo: '))
contador(inicio, fim, pulo)
