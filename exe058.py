import random
print('\033[43m               ADIVINHANDO O NÚMERO               \033[m')
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
computador = random.choice(lista)
meupalpite = int(input('Tente adivinhar o número que escolhi entre 0 e 10: '))
falha = 1
if computador == meupalpite == 0:
    print('Muito bom! Você só precisou de {} tentativa.'.format(falha))
else:
    while computador != meupalpite:
        meupalpite = int(input('Tente mais uma vez: '))
        falha += 1

        if computador == meupalpite:
            print('Parabéns! Você precisou de [\033[32m{}\033[m] tentativas.'.format(falha))

print('Eu escolhi o número [\033[33m{}\033[m]'.format(computador))
print('O seu palpite foi [\033[32m{}\033[m]'.format(meupalpite))
