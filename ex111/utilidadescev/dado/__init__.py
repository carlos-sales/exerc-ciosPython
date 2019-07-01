def leiaDinheiro(msg):
    val = input(msg).strip().replace(',', '.')
    while not val.isdecimal():
        print(f'\033[1;91mERRO: {val} não é um valor monetário. Tente novamente.\033[0;0m')
        val = input(msg)
    return val
