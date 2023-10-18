print('=' * 30)
print('{:^30}'.format('Caixa Eletrônico'))
print('=' * 30)
valor = int(input('Quanto deseja sacar? R$ '))
print(f'O valor solicitado foi: {valor}')
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre!')
