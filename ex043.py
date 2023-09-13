peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Abaixo do Peso.')
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Peso ideal.')
elif 25 <= imc < 30:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Obesidade')
else:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Obesidade mórbida')
