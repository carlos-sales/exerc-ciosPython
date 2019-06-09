boletim = []
while True:
    aluno = []
    notas = []
    aluno.append(str(input('Digite o nome: ').strip()))
    notas.append(float(input('Digite a primeira nota: ')))
    notas.append(float(input('Digite a segunda nota: ')))
    aluno.append(notas[:])
    boletim.append(aluno[:])
    aluno.clear()
    notas.clear()
    resp = ''
    while True:
        resp = str(input('Deseja continuar [S/N]? ').upper())
        if resp == 'S' or resp == 'N':
            break
    if resp == 'N':
        break
print('-='*10)
print('Nº   NOME           MEDIA')
for pos, i in enumerate(boletim):
    print(f'{pos:<5}{i[0]:<15}{(i[1][0] + i[1][1])/2:>3}')
while True:
    alu = int(input('Mostrar notas de qual aluno (digite o número correspondente ou 999 para sair): '))
    if alu == 999:
        break
    else:
        print(f'Notas de {boletim[alu][0]}: {boletim[alu][1][0]} e {boletim[alu][1][1]}')
