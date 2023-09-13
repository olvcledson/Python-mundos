velo = float(input('Qual a velocidade do carro: '))
if velo > 80.0:
    n1 = velo - 80.0
    n2 = n1 * 7.0
    print('A velocidade está acima da media (80km/h). Você será multado em {}R$.'.format(n2))
else:
    print('Tenha ium bom dia, dirija com segurança!')
