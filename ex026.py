frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "a" aparece {} vezes na frase'.format(frase.count('A')))
print('A letra "a" aparece na {}° posição da frase'.format(frase.find('A')+1))
print('A ultima letra "a" aparecei na posição {}'.format(frase.rfind('A')+1))