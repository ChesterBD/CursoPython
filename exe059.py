print('\033[43m        EXEMPLO DE MENU        \033[m')
opcao = 0
n1 = int(input('Entre com o 1º número: '))
n2 = int(input('Entre com o 2º número: '))

print('=============================')
while opcao != 5:
    opcao = int(input("""O que deseja fazer com os números?
[\033[31m1\033[m] SOMAR
[\033[31m2\033[m] MULTIPLICAR
[\033[31m3\033[m] SABER QUAL É O MAIOR
[\033[31m4\033[m] TROCAR NÚMEROS
[\033[31m5\033[m] SAIR
Opção: """))

    if opcao == 1:
        print('A soma entre {} e {} é: [{}]'.format(n1, n2, n1 + n2))
        opcao = 5
    elif opcao == 2:
        print('A multiplicação entre {} e {} é: [{}]'.format(n1, n2, n1 * n2))
        opcao = 5
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
            opcao = 5
        else:
            print('{} é maior que {}'.format(n2, n1))
            opcao = 5
    if opcao == 4:
        n1 = int(input('Entre com outro 1º número: '))
        n2 = int(input('Entre com outro 2º número: '))
