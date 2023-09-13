n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O valor {} é MAIOR que o segundo'.format(n1))
elif n2 == n1:
    print('O valores são iguais.')
else:
    print('O valor {} é MAIOR que o primeiro'.format(n2))
