frase = str(input('Digite uma frase: ').strip().lower())
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A letra A aparece a primeira vez na posição: {}'.format(frase.find('a') +1))
print('A letra A aparece pela última vez na posição: {}'.format(frase.lower().rfind('a') +1))