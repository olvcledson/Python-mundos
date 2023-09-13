a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < c + a and c < a + b:
    print('Os segmentos acima podem formar triângulo')
    if a == b and b == c:
        print('EQUILÁTERO: todos os lados iguais')
    elif a == b and b != c or a == c and b != c or b == c and c != a:
        print('ISÓSCELES: dois lados iguais, um diferente')
    elif a != b and b != c or a != c:
        print('ESCALENO: todos os lados diferentes')
else:
    print('Os segmentos acima NÃO podem formar triângulo')
