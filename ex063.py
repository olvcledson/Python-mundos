print('-' * 10, 'SEQUÊNCIA FIBONACCI', '-' * 10)
n = int(input('Quanto termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~~~~~'*n)
print('{} -> {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')

