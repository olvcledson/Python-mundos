from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
menu = 0
while menu != 5:
    print('-'*5, 'MENU', '-'*5)
    menu = int(input('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
Opção: '''))
    if menu == 1:
        s = n1 + n2
        print('A soma entre {} e {} é: {}'.format(n1, n2, s))
    elif menu == 2:
        m = n1 * n2
        print('A multiplicação entre {} e {} é de: {}'.format(n1, n2, m))
    elif menu == 3:
        maior = n1 and n2
        if n1 > n2:
            print('O maior valor é {}, primeiro valor'.format(n1))
        else:
            print('O maior valor é {}, segundo valor'.format(n2))
    elif menu == 4:
        print('Informe os número novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif menu == 5:
        print('Você saiu do programa, até a próxima.')
    else:
        print('Opção inválida. Tente novamente.')
    print('=---=' * 8)
    sleep(2)
print('TCHAUUUUU!')