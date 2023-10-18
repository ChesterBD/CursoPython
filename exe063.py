print('\033[42m              SEQUÊNCIA DE FIBONACCI              \033[m')
termos = int(input('Quantos termos da sequência você deseja exibir? '))
print('-' * 50)
t1 = 0
t2 = 1
cont = 3
print('{}, {},'.format(t1, t2), end=' ')
while cont <= termos:
    t3 = t1 + t2
    print('{},'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim da Sequência!')

# Modelo de Fionacci (0, 1, 1, 2, 3, 5, 8, 13, ...)
