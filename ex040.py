n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media <= 5.0:
    print('Sua media foi: {:.1f}'.format(media))
    print('Média abaixo de 5.0: Reprovado.')
elif media > 5 and media < 6.9:
    print('Sua media foi: {:.1f}'.format(media))
    print('Sua média está entre 5.0 e 6.9: Recuperação.')
else:
    print('Sua media foi: {:.1f}'.format(media))
    print('Está acima da média que é 7.0: Aprovado.')
