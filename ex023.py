numero = int(input('Digite um número entre 0 a 9999: '))
uni = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print('A unidade é: {}'.format(uni))
print('A dezena é: {}'.format(dez))
print('A centena é: {}'.format(cen))
print('A milhar é: {}'.format(mil))

