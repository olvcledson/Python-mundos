maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa? '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menos peso lido foi de {}kg'.format(menor))
