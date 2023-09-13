print('Gerador de PA')
print('-=' * 10)
t = int(input('Digite o primeiro termo: '))
r = int(input('Razão da PA: '))
termo = t
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(t), end='')
        t += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quatos termos você quer mostrar a mais? '))
print('Fim, termos {}.'.format(total))