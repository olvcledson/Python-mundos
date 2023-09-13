n1 = float(input('Qual é o preço do produto? R$'))
d = n1 * 0.05
print('O produto com 5% de desconto ficará em: R${:.3} e o total será: R$ {:.5}'.format(d, n1-d))
