# exp = list()
exp = (str(input('Digite a expressão: ')))
ab = exp.split('(')
fe = exp.split(')')
if len(ab) == len(fe):
    print('Expressão válida!')
else:
    print('Expressão inválida =(')
