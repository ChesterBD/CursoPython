from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pessoa in range(1, 6):
    nascimento = int(input('Entre com a data de nascimento: '))
    idade = atual - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Tem {} pessoas menor(es) de idade'.format(menor))
print('Tem {} pessoas maior(es) de idade'.format(maior))
