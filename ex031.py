dis = float(input('Qual a distância da viagem: '))
print('A viagem será de {}Km.'.format(dis))
if dis <= 200:
    preco = dis * 0.50
else:
    preco = dis * 0.45
print('Sua viagem ficará no valor de R${:.2f}'.format(preco))
