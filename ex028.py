import random

num = random.randint(0, 5)
num1 = int(input('Digite um número entre 0 e 5: '))
if num1 == num:
    print('Você acertou!')
else:
    print('Você errou!')
print('O número era: {}'.format(num))
