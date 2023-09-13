from datetime import date

ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Você tem {}'.format(idade))
    print('Atleta: MIRIM.')
elif 9 < idade < 14:
    print('Você tem {}'.format(idade))
    print('Atleta: INFANTIL.')
elif 14 < idade < 19:
    print('Você tem {}'.format(idade))
    print('Atleta: JUNIOR.')
elif 19 < idade < 25:
    print('Você tem {}'.format(idade))
    print('Atleta: SÊNIOR.')
else:
    print("Você tem {}".format(idade))
    print('Atleta: MASTER.')
