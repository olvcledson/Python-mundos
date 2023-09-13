resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
media = soma / quant
print('Você digitou {} números e a média foi {}.'.format(quant, media))
print('O maior {} e o menor {}'.format(maior, menor))
