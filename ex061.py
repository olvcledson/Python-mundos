print('Gerador de PA')
print('-=' * 10)
t = int(input('Digite o primeiro termo: '))
r = int(input('Razão da PA: '))
termo = t
cont = 1
while cont <= 10:
    print('{} -> '.format(t), end='')
    t += r
    cont += 1
print('Acabou!')