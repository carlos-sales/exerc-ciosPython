alt = float(input('Digite a altura, em metros: '))
peso = float(input('Digite o peso, em quilogramas: '))

imc = peso / (alt ** 2)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
