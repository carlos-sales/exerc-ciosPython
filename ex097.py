def escreva(msg):
    esp = len(msg)+4
    print('~' * esp)
    print(f'{msg:^{esp}}')
    print('~' * esp)


escreva('Carlos Alberto')
escreva('Curso de Python no Youtube')
escreva('CeV')
