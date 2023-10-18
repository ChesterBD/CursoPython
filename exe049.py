print('\033[45m       TABUADA       \033[m')
num = int(input('Digite um número: '))
for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(num, c, num*c))
