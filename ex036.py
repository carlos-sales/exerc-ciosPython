val = float(input('Informe o valor da casa: R$ '))
sal = float(input('Informe seu salário: R$ '))
anos = int(input('Informe em quantos anos pretende fazer o pagamento: '))

limite_prest = sal * 0.3
prest = val / (anos * 12)

if prest < limite_prest:
    print('O empréstimo foi aprovado e o valor da prestação será R$ {:.2f}'.format(prest))
else:
    print('Desculpe, mas o empréstimo não foi aprovado para os parâmetros informados')
