import math
ângulo = float(input('Digita um ângulo: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print('O valor do seno é {:.2f}, cosseno {:.2f} e tangente {:.2f} desse ângulo {}'.format(seno, cosseno, tangente,ângulo))
