print('\033[43m    ADICIONANDO NÚMEROS EM UMA LISTA    \033[m')
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Entre com o {c + 1}º número: ')))
print('=' * 40)
print(f'Os números que você digitou foram: \n{valores}')
print('=' * 40)
for c, v in enumerate(valores):
    print(f'Na posição [{c}] está o número {v}')
print('=' * 40)
print(f'O menor número é o [{min(valores)}] e o maior é o [{max(valores)}]')
