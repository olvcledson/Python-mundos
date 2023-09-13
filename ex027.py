nome = str(input('Digite seu nome: ')).strip()
divisão = nome.split()
print('O primeiro nome é: {}'.format(divisão[0]))
print('O ultimo nome é {}'.format(divisão[len(divisão)-1]))

