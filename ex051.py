t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
décimo = t + (10 - 1) * r
for c in range(t, décimo + r, r):
    print(c, end=' -> ')
print('ACABOU!')
