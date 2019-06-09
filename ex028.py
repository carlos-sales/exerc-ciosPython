from random import randint
n = randint(0, 5)
adv = int(input('Tente adivinhar, digite um número: '))
if n == adv:
    print('Parabéns, você brilhou')
else:
    print('ERROOOOOOOOOOOOU')
