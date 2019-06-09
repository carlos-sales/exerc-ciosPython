soma = 0
qtd = 0
while True:
    n = int(input('Digite um número [999 para sair]: '))
    if n == 999: break
    soma += n
    qtd +=1
print(f'Foram digitados {qtd} números\nSoma dos números: {soma}')
