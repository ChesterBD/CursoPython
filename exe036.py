print('\033[47m Empréstimo Pessoal \033[m')
vi = float(input('Digite o valor do imóvel a ser financiada: R$ '))
s = float(input('Digite seu salário: R$ '))
t = float(input('Em quantos anos pretende financiar?: '))
vp = vi/(t*12)
if vp < (s * 0.3):
    print('Parabéns, seu empréstimo foi \033[42m aprovado! \033[m')
    print('O valor do imóvel é de R$ {:.2f}, divididos em {} prestações de R$ {:.2f}' .format(vi, t*12, vp))
else:
    print('Infelizmente seu empréstimo foi \033[37:41m negado! \033[m')
    print('A prestação mensal de R$ {:.2f} excede os 30% do seu salário!'.format(vp))
