print('Sequência de Fibonacci')
qtd = int(input('Digite quantos elementos deseja exibir: '))
term1 = 0
term2 = 1
print('{} → {} → '.format(term1, term2), end='')
i = 3 #contador inicia em 3, pois os dois primeiros termos da sequencia são pré definidos
while i <= qtd:
    termN = term1 + term2
    print('{} → '.format(termN), end='')
    term1 = term2
    term2 = termN
    i += 1
print(' FIM')
