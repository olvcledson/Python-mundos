sexo = str(input('Qual o seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Opção inválida, digite novamente: ')).upper().strip()[0]
print('Certo, você é do sexo {}. Obrigado!'.format(sexo))
