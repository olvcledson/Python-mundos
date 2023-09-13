salario = float(input('Qual o valor do funcionário: R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O salário teve aumento e passa a ganhar {:.2f}'.format(novo))
