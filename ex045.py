import random
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
nome = str(input('Qual é o nome do jogador: '))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('{} jogou {}'.format(nome, itens[jogador]))
print('-=' * 11)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE: Os jogadores escolheram PEDRA')
    elif jogador == 1:
        print('VITORIA DO {}'.format(nome))
    elif jogador == 2:
        print('VITORIA DO COMPUTADOR')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print('VITORIA DO COMPUTADOR')
    elif jogador == 1:
        print('EMPATE: Os jogadores escolheram PAPEL')
    elif jogador == 2:
        print('VITORIA DO {}'.format(nome))
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print('VITORIA DO {}'.format(nome))
    elif jogador == 1:
        print('VITORIA DO COMPUTADOR')
    elif jogador == 2:
        print('EMPATE: Os jogadores escolheram TESOURA')
    else:
        print('JOGADA INVÁLIDA!')
