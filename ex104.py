def leiaInt(msg):
    num = input(msg)
    while not num.isnumeric():
        print('\033[31mERRO: Digite um número inteiro\033[0;0m')
        num = input(msg)
    return num


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
