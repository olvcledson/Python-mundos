times = ('Botafogo', 'Palmeiras', 'Bragantino','Grêmio', 'Flamengo', 'Fluminense', 'Athletico-PR', 'Fortaleza', 'Atlético-MG',
         'Cuiabá', 'Cruzeiro', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Goiás', 'Santos', 'Vasco',
         'América-MG', 'Coritiba')
print('=-'*75)
print(f'Lista de time do brasileirão 2023: {times}')
print('=-'*75)
print(f'Os 5 primeiros colocados são: {times [0:5]}')
print('=-'*75)
print(f'Os 4 últimos colocados são: {times [-4:]}')
print('=-' * 75)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-' * 75)
print(f'O Corinthians está na posição: {times.index("Corinthians")+1}° posição')