from math import factorial
print('\033[43m            CALCULANDO O FATORIAL DE UM NÚMERO            \033[m')
n = int(input('Entre com um número inteiro para calcular seu Fatorial: '))
c = n
f = 1
print('----------------------------------------------------------')
print('Calculando o {}!'.format(n))
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    f *= c
    c -= 1
print('\033[42;52m {} \033[m'.format(f))

#print(factorial(n)) Essa é a outra maneira de se obter um fatorial.
