n = cont = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A quantidade de números foi {cont} e a soma entre eles é de {soma}.')
