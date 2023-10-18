import random
lista = [0,1,2,3,4,5]
print('Tente adivinhar o número entre 0 e 5 que eu estou pensando!')
n = int(input('Digite um número: '))
c = random.choice(lista)

if n == c:
    print('Parabéns, você acertou! \nO número era {} mesmo!'.format(n))
else:
    print('Ainda não. Tente novamente!')
    print('O número era {}!'.format(c))
