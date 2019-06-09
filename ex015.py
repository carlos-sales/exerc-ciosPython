print('==== Aluguel de Carros ====')
dias = int(input('Digite a quantidade de dias em que o carro foi alugado: '))
km = float(input('Digite a quilometragem percorrida pela carro: '))
val = dias * 60
val += km * 0.15
print("Valor total a pagar: R$ {:.2f}".format(val))
