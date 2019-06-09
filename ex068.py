from random import randint
from time import sleep
placarPlayer = 0
placarCPU = 0
print('º~'*20)
print('PAR OU ÍMPAR')
print('º~'*30)
while True:
    numPlayer = int(input('Digite um número: '))
    escPlayer = str(input('Você quer PAR ou ÍMPAR? [P/I] ').upper())
    if escPlayer != 'P' and escPlayer != 'I':
        print('Você escolheu uma opção inválida')
    else:
        numCPU = randint(0, 10)
        if escPlayer == 'P':
            escCPU = 'I'
        elif escPlayer == 'I':
            escCPU = 'P'
        soma = numCPU + numPlayer
        print('UM! ', end='')
        sleep(1)
        print('DOIS! ', end='')
        sleep(1)
        print('TRÊS! ', end='')
        sleep(1)
        print('JÁAAAA!')
        sleep(1)
        print(f'Você jogou {numPlayer}\nCPU jogou {numCPU}')
        if soma % 2 == 0:
            if escPlayer == 'P':
                print('Você ganhou!')
                placarPlayer += 1
                print('-' * 20)
            else:
                print('Você perdeu!')
                placarCPU += 1
                break
        else:
            if escPlayer == 'I':
                print('Você ganhou!')
                placarPlayer += 1
                print('-' * 20)
            else:
                print('Você perdeu!')
                placarCPU += 1
                break
print('-'*20)
print(f'O JOGO TERMINOU!!!\nPlayer {placarPlayer} X {placarCPU} CPU')
