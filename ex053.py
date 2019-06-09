frase = str(input('Insira a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for i in range(len(junto)-1, -1, -1):
    inverso += junto[i]
if junto == inverso:
    print('É palíndromo')
else:
    print('NÃO É palíndromo')
