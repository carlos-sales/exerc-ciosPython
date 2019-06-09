frase = str(input('Digite a frase: ')).strip()
print('Qtd "a": {}'.format(frase.lower().count('a')))
print('Primeiro em: {}'.format(frase.lower().find('a')))
print('Último em: {}'.format(frase.lower().rfind('a')))
