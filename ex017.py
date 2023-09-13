import math
num1 = float(input('Valor do cateto oposto: '))
num2 = float(input('Valor do cateto adjacente: '))
cato = num1 ** 2
cata = num2 ** 2
hipo = cato + cata
print('O cateto oposto é de {:.2f} e o adjacente é de {:.2f} o valor da hipotenusa será de {:.2f}'.format(cato, cata, math.sqrt(hipo)))
