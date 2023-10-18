num = int(input('Entre com um número: '))
while num > 0:
    print(num, end=' ')
    print(' > ' if num > 1 else 'Fim!', end=' ')
    num -= 1
