sex = ''
while sex != 'M' and sex != 'F':
    sex = str(input('Digite seu sexo [M/F]: ').upper())
    if sex != 'M' and sex != 'F':
        print('Você digitou um sexo inválido')
