a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < c + a and c < a + b:
    print('Os segmentos acima podem formar triângulo')
else:
    print('Os segmentos acima NÃO podem formar triângulo')