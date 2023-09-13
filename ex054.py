from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1, 8):
    nasc = int(input('Em que ano {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 27:
        totmaior += 1
    else:
        totmenor += 1
print('{} Maiores'. format(totmaior))
print('{} Menores'.format(totmenor))

