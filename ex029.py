v = int(input('Digite sua velocidade em Km/h: '))
lim = 80
multa = (v-80)*7
if v <= lim:
    print('Você está dentro do limite de velocidade!')
else:
    print('Ops! Você foi multado por estar acima do limite de velocidade permitido!')
    print('Você foi multado em: R${}'.format(multa))