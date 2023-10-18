print('\033[43m    ADICIONANDO NÚMEROS EM UMA LISTA [2]    \033[m')
valores = []
op = 'S'
while op == 'S':
    num = int(input('Entre com um número: '))
    if num in valores:
        print('Esse número já existe!')
    else:
        print('Valor adicionado com sucesso!')
        valores.append(num)
    op = str(input('Deseja adicionar outro número? [S/N]: ').upper())
print('=' * 40)
print(f'Os números digitados foram: {sorted(valores)}')
