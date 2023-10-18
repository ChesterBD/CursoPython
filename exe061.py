print('\033[43m          TERMOS DE UMA PA          \033[m')
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Entre com a razão: '))
cont = 1
termo = a1
while cont <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += r
    cont += 1
print('\033[31m Fim \033[m')
