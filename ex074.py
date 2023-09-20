from random import randint
número = (randint(0, 10), randint(0, 10),
     randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valor sorteados foram: ', end='')
for n in número:
    print(f'{n}', end=' ')
print(f'\nO maior sorteado foi: {max(número)}')
print(f'O menor sorteado foi: {min(número)}')
