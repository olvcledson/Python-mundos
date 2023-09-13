from datetime import date

sexo = int(input('Digite 1 se for homem e 2 se for mulher: '))
if sexo == 1:
    ano = int(input('Digite o ano de seu nascimento(YYYY): '))
    idade = date.today().year - ano
    print('Sua idade é {}'.format(idade))
    if idade > 18:
        ano = ano + (idade - 18)
        print('Você já passou do tempo do alistamento. Já passou {} ano(s).'.format(idade - 18))
        print('Seu alistamento foi em {}'.format(ano))
    elif idade == 18:
        print('Você está apto a se alistar!')
    else:
        ano = ano - (idade - 18)
        print('Você ainda vai se alistar ao serviço militar, faltam {} ano(s).'.format(18 - idade))
        print('Seu alistamento será em {}'.format(ano))
else:
    print('Você não precisa se alistar')
