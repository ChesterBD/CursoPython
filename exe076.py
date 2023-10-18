listagem = ('lápis', 1.45, 'borracha', 0.39, 'caderno', 5, 'estojo', 12.45, 'transferidor',
            4, 'compasso', 3.75, 'mochila', 175.50, 'canetas', 8.50, 'livro', 34.69)
print('\033[43m        LISTAGEM DE PREÇOS        \033[m')
for pos in range(0, len(listagem), 2):
    print(f'{listagem[pos]:*<20}'.capitalize(), 'R$' f'{listagem[pos+1]:>8.2f}')
print('='*35)
