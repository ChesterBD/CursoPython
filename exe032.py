y = int(input('Digite um ano para saber se ele é bissexto: '))
if (y % 4 or y % 400) == 0:
    print('Esse ano é Bissexto!')
elif y % 100 != 0:
    print('Esse ano é Bissexto!')
else:
    print('Esse ano não é Bissexto!')
