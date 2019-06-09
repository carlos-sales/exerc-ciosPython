from random import randint
from time import sleep
nome = str(input('Digite seu nome: '))
opcoes = ('Pedra', 'Papel', 'Tesoura')
op = 0
pj = 0
pc = 0
while op != 3:

    print('PLACAR: {} {} X {} Computador'.format(nome, pj, pc))
    print(' ---- JOKENPÔ ---- ')
    print('| 0 - Pedra       |')
    print('| 1 - Papel       |')
    print('| 2 - Tesoura     |')
    print('| 3 - Sair        |')
    print(' ----------------- ')
    op = int(input('Digite sua jogada: '))
    opc = randint(0, 2)

    if op != 3:
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ!!!')
        sleep(1)
        print('-=' * 20)
        print('{}: {} X {} :Computador'.format(nome, opcoes[op], opcoes[opc]))
        print('-=' * 20)

    if op == 0 and opc == 2:
        print('{} VENCEU!'.format(nome))
        pj += 1
    elif op == 0 and opc == 1:
        print('Computador VENCEU!')
        pc += 1
    elif op == 1 and opc == 0:
        print('{} VENCEU!'.format(nome))
        pj += 1
    elif op == 1 and opc == 2:
        print('Computador VENCEU!')
        pc += 1
    elif op == 2 and opc == 1:
        print('{} VENCEU!'.format(nome))
        pj += 1
    elif op == 2 and opc == 0:
        print('Computador VENCEU!')
        pc += 1
    elif op == opc:
        print('EMPATE!')
    elif op == 3:
        print('Bom jogo!')
        print('Placar final: {} {} X {} Computador'.format(nome, pj, pc))
        if pj > pc:
            print('Parabéns! Você venceu!')
        elif pj == pc:
            print('Empatou!')
        else:
            print('Você perdeu!')
    else:
        print('Opção inválida!')
