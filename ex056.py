iVelho = 0
nVelho = ''
media = 0
mVinte = 0
for i in range(0, 4):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo (m/f): '))
    if sexo == 'm':
        if idade > iVelho:
            iVelho = idade
            nVelho = nome
    else:
        if idade < 20:
            mVinte += 1
    media += idade
media /= 4
print('Homem mais velho: {}'.format(nVelho))
print('Mulheres com menos de 20 anos: {}'.format(mVinte))
print('Média de idades: {}'.format(media))
