print('\033[46m      NÚMERO PRIMO      \033[m')
num = int(input('Entre com um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end=' ')
        tot += 1
    else:
        print('\033[33m', end=' ')
    print(c, end=' | ')
print('\nO número {} é divisível por {} números'.format(num, tot))
if tot == 2:
    print('Por isso ele é \033[52m Primo! \033[m')
else:
    print('Por isso, \033[51m não é Primo! \033[m')
