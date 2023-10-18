s = int(input('Digite o valor do seu Salário atual: R$'))
if s > 1250:
    print('Seu Salário teve um aumento de 10% e vai para R${:.2f}'.format(s + (s * 0.1)))
else:
    print('Seu Salário teve um aumento de 15% e vai para R${:.2f}'.format(s + (s * 0.15)))
