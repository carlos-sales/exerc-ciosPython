ld1 = int(input('Lado 1: '))
ld2 = int(input('Lado 2: '))
ld3 = int(input('Lado 3: '))
if ((ld2 - ld3) < ld1 < (ld2 + ld3)) and ((ld1 - ld3) < ld2 < (ld1 + ld3)) and ((ld2 - ld1) < ld3 < (ld2 + ld1)):
    print('Pode formar um triângulo =)')

    if ld2 == ld1 and ld2 == ld3 and ld1 == ld3:
        print('Será um triângulo equilátero')
    elif ld2 == ld1 or ld2 == ld3 or ld1 == ld3:
        print('Será um triângulo isósceles')
    else:
        print('Será um triângulo escaleno')

else:
    print('Não pode se tornar um triângulo =(')
