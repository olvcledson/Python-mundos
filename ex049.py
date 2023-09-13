numero = int(input('Digite um número: '))
print('-' * 12)
for n1 in range(1, 11):
    resultado = numero * n1
    print('{} x {} = {}'.format(numero, n1, resultado))

