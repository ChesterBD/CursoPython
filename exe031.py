d = int(input('Digite, em Km, a distância a ser percorrida: '))
p1 = d * 0.50
p2 = d * 0.45
if d > 200:
    print('O valor da passagem é: R${:.2f}'.format(p2))
else:
    print('O valor da passagem é:R${:.2f}'.format(p1))
