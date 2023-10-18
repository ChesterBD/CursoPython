soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} número(s) pare e a soma deles é {}'.format(cont, soma))
