from time import sleep
print('-=' * 3, 'Contagem regressiva', '-=' * 3)
for cont in range(10, -1, -1):
    sleep(1)
    print(cont)
sleep(1)
print('FELIZ ANO NOVO!')
