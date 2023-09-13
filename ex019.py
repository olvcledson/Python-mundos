import random

nome1 = str(input('Primeira opção: '))
nome2 = str(input('Segunda opção '))
nome3 = str(input('Terceira opção: '))
lista = [nome1, nome2, nome3]
escolhido = random.choice(lista)
print('Os babys serão: {}'.format(escolhido))
