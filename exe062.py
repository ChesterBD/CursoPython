print('\033[43;36m          TERMOS DE UMA PA          \033[m')
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Entre com a razão: '))
cont = 1
termo = a1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{}'.format(termo), end=' -> ')
        termo += r
        cont += 1
    print('Pausa!')
    mais = int(input('Quantos termos à mais você quer? '))
print('A PA foi finalizada e o total de termos exibidos foi: [\033[31m{}\033[m]'.format(total))
