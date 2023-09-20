palavras = ('bisneta', 'tio', 'pai', 'nora',
            'madrasta', 'primo', 'filho',
            'avo', 'prima')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
