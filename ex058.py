from random import randint
print('Estou pensando em um número entre 0 e 10...')
num = randint(0, 10)
palp = 0
mNum = -1
while num != mNum:
    mNum = int(input('Tente acertar o número: '))
    palp += 1
    if num != mNum:
        print('Errooooou!')
print('Parabéns, você brilhou!\nNumero: {}\nTentativas: {}'.format(num, palp))
