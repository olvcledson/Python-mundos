import random
total = 0
v = 0
while True:
    print('=-'*15)
    print('VAMOS JOGAR PAR OU IMPAR')
    print('=-'*15)
    jogador = int(input('Diga um valor: '))
    computador = random.randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. O total de {total} deu: ')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == '1':
        if total % 2 == 1:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
        print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')