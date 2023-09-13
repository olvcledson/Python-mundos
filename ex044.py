print('{:=^40}'.format(' LOJAS DINHO '))
preço = float(input('Qual o valor a ser pago: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    dinheiro = preço - (preço * 0.10)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no preço final.'.format(preço, dinheiro))
elif opção == 2:
    à_vista = preço - (preço * 0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no preço final.'.format(preço, à_vista))
elif opção == 3:
    duas_vezes = preço / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(duas_vezes))
elif opção == 4:
    tres_vezes = preço + (preço * 0.20)
    totparc = int(input('Quantas parcelas? '))
    parcela = tres_vezes / totparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totparc, parcela))
else:
    print('OPÇÂO INVÁLIDA! ')
